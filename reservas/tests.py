from datetime import date, timedelta
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Espacio, PerfilUsuario, Reserva

User = get_user_model()

class ReservaModelTests(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username="ana", password="Prueba-segura-123")
        self.espacio = Espacio.objects.create(nombre="Aula 101", codigo="A101", ubicacion="Bloque A", capacidad=25)
        self.fecha = timezone.localdate() + timedelta(days=1)

    def crear(self, inicio="09:00", fin="10:00", **kwargs):
        from datetime import time
        h1 = time.fromisoformat(inicio)
        h2 = time.fromisoformat(fin)
        reserva = Reserva(solicitante=self.usuario, espacio=self.espacio, fecha=self.fecha, hora_inicio=h1, hora_fin=h2, motivo="Clase de prueba", **kwargs)
        reserva.save()
        return reserva

    def test_reserva_valida_se_guarda(self):
        reserva = self.crear()
        self.assertEqual(reserva.estado, Reserva.Estado.PENDIENTE)

    def test_rechaza_fin_igual_o_antes_del_inicio(self):
        from datetime import time
        reserva = Reserva(solicitante=self.usuario, espacio=self.espacio, fecha=self.fecha, hora_inicio=time(10), hora_fin=time(9), motivo="Inválida")
        with self.assertRaises(ValidationError):
            reserva.save()

    def test_rechaza_duracion_superior_a_cuatro_horas(self):
        with self.assertRaises(ValidationError):
            self.crear("08:00", "12:01")

    def test_acepta_duracion_exacta_de_cuatro_horas(self):
        reserva = self.crear("08:00", "12:00")
        self.assertEqual(reserva.duracion, timedelta(hours=4))

    def test_impide_solapamiento_mismo_espacio(self):
        self.crear("09:00", "10:30")
        with self.assertRaises(ValidationError):
            self.crear("10:00", "11:00")

    def test_permite_horarios_contiguos(self):
        self.crear("09:00", "10:00")
        segunda = self.crear("10:00", "11:00")
        self.assertIsNotNone(segunda.pk)

    def test_rechazada_no_bloquea_horario(self):
        primera = self.crear("09:00", "10:00")
        primera.estado = Reserva.Estado.RECHAZADA
        primera.save()
        segunda = self.crear("09:30", "10:30")
        self.assertIsNotNone(segunda.pk)

    def test_rechaza_fecha_pasada(self):
        from datetime import time
        reserva = Reserva(solicitante=self.usuario, espacio=self.espacio, fecha=timezone.localdate()-timedelta(days=1), hora_inicio=time(9), hora_fin=time(10), motivo="Pasada")
        with self.assertRaises(ValidationError):
            reserva.save()

class ReservaViewTests(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username="solicitante", password="Prueba-segura-123")
        self.gestor = User.objects.create_user(username="gestor", password="Prueba-segura-123")
        perfil = PerfilUsuario.objects.get(usuario=self.gestor)
        perfil.rol = PerfilUsuario.Rol.GESTOR
        perfil.save()
        self.espacio = Espacio.objects.create(nombre="Laboratorio 1", codigo="LAB1", ubicacion="Bloque B", capacidad=20)
        self.fecha = (timezone.localdate()+timedelta(days=1)).isoformat()

    def test_inicio_requiere_autenticacion(self):
        response = self.client.get(reverse("inicio"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_solicitante_puede_crear_reserva(self):
        self.client.login(username="solicitante", password="Prueba-segura-123")
        response = self.client.post(reverse("crear_reserva"), {"espacio": self.espacio.pk, "fecha": self.fecha, "hora_inicio": "09:00", "hora_fin": "10:00", "motivo": "Práctica académica"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reserva.objects.count(), 1)
        self.assertEqual(Reserva.objects.first().solicitante, self.usuario)

    def test_solicitante_no_puede_aprobar(self):
        from datetime import time
        reserva = Reserva.objects.create(solicitante=self.usuario, espacio=self.espacio, fecha=timezone.localdate()+timedelta(days=1), hora_inicio=time(9), hora_fin=time(10), motivo="Clase")
        self.client.login(username="solicitante", password="Prueba-segura-123")
        response = self.client.post(reverse("aprobar_reserva", args=[reserva.pk]))
        self.assertEqual(response.status_code, 403)

    def test_gestor_puede_aprobar_pendiente(self):
        from datetime import time
        reserva = Reserva.objects.create(solicitante=self.usuario, espacio=self.espacio, fecha=timezone.localdate()+timedelta(days=1), hora_inicio=time(9), hora_fin=time(10), motivo="Clase")
        self.client.login(username="gestor", password="Prueba-segura-123")
        response = self.client.post(reverse("aprobar_reserva", args=[reserva.pk]))
        reserva.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(reserva.estado, Reserva.Estado.APROBADA)
        self.assertEqual(reserva.revisado_por, self.gestor)

    def test_usuario_no_puede_ver_reserva_ajena(self):
        from datetime import time
        reserva = Reserva.objects.create(solicitante=self.usuario, espacio=self.espacio, fecha=timezone.localdate()+timedelta(days=1), hora_inicio=time(9), hora_fin=time(10), motivo="Clase")
        otro = User.objects.create_user(username="otro", password="Prueba-segura-123")
        self.client.login(username="otro", password="Prueba-segura-123")
        response = self.client.get(reverse("detalle_reserva", args=[reserva.pk]))
        self.assertEqual(response.status_code, 403)
