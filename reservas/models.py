from datetime import datetime, timedelta
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class PerfilUsuario(models.Model):
    class Rol(models.TextChoices):
        SOLICITANTE = "solicitante", "Solicitante"
        GESTOR = "gestor", "Gestor de espacios"
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="perfil")
    rol = models.CharField(max_length=20, choices=Rol.choices, default=Rol.SOLICITANTE)

    def __str__(self):
        return f"{self.usuario.username} ({self.get_rol_display()})"

class Espacio(models.Model):
    nombre = models.CharField(max_length=120)
    codigo = models.CharField(max_length=20, unique=True)
    ubicacion = models.CharField(max_length=160)
    capacidad = models.PositiveIntegerField(default=1)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Reserva(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        APROBADA = "aprobada", "Aprobada"
        RECHAZADA = "rechazada", "Rechazada"
        CANCELADA = "cancelada", "Cancelada"

    solicitante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="reservas")
    espacio = models.ForeignKey(Espacio, on_delete=models.PROTECT, related_name="reservas")
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    motivo = models.CharField(max_length=250)
    estado = models.CharField(max_length=12, choices=Estado.choices, default=Estado.PENDIENTE)
    revisado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="reservas_revisadas")
    observaciones = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-fecha", "hora_inicio"]
        indexes = [models.Index(fields=["espacio", "fecha", "estado"], name="res_esp_fecha_estado_idx")]

    def clean(self):
        errores = {}
        if self.hora_inicio and self.hora_fin:
            inicio = datetime.combine(self.fecha or timezone.localdate(), self.hora_inicio)
            fin = datetime.combine(self.fecha or timezone.localdate(), self.hora_fin)
            if fin <= inicio:
                errores["hora_fin"] = "La hora de finalización debe ser posterior a la hora de inicio."
            elif fin - inicio > timedelta(hours=4):
                errores["hora_fin"] = "La reserva no puede superar cuatro horas consecutivas."
        if self.fecha and self.fecha < timezone.localdate():
            errores["fecha"] = "No se pueden crear reservas para fechas pasadas."
        if self.espacio_id and self.fecha and self.hora_inicio and self.hora_fin and self.hora_fin > self.hora_inicio:
            estados_ocupados = [self.Estado.PENDIENTE, self.Estado.APROBADA]
            conflictos = Reserva.objects.filter(
                espacio_id=self.espacio_id, fecha=self.fecha, estado__in=estados_ocupados,
                hora_inicio__lt=self.hora_fin, hora_fin__gt=self.hora_inicio,
            )
            if self.pk:
                conflictos = conflictos.exclude(pk=self.pk)
            if conflictos.exists():
                errores["hora_inicio"] = "El espacio ya tiene una reserva pendiente o aprobada en ese horario."
        if errores:
            raise ValidationError(errores)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    @property
    def duracion(self):
        inicio = datetime.combine(self.fecha, self.hora_inicio)
        fin = datetime.combine(self.fecha, self.hora_fin)
        return fin - inicio

    def __str__(self):
        return f"{self.espacio.codigo} - {self.fecha} {self.hora_inicio}-{self.hora_fin}"
