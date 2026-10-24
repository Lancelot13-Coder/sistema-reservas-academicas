# Generated manually for the starter project; verify with `python manage.py makemigrations --check`.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name="Espacio", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=120)), ("codigo", models.CharField(max_length=20, unique=True)), ("ubicacion", models.CharField(max_length=160)), ("capacidad", models.PositiveIntegerField(default=1)), ("descripcion", models.TextField(blank=True)), ("activo", models.BooleanField(default=True)), ("creado_en", models.DateTimeField(auto_now_add=True))], options={"ordering": ["nombre"]}),
        migrations.CreateModel(name="PerfilUsuario", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("rol", models.CharField(choices=[("solicitante", "Solicitante"), ("gestor", "Gestor de espacios")], default="solicitante", max_length=20)), ("usuario", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="perfil", to=settings.AUTH_USER_MODEL))]),
        migrations.CreateModel(name="Reserva", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("fecha", models.DateField()), ("hora_inicio", models.TimeField()), ("hora_fin", models.TimeField()), ("motivo", models.CharField(max_length=250)), ("estado", models.CharField(choices=[("pendiente", "Pendiente"), ("aprobada", "Aprobada"), ("rechazada", "Rechazada"), ("cancelada", "Cancelada")], default="pendiente", max_length=12)), ("observaciones", models.TextField(blank=True)), ("creado_en", models.DateTimeField(auto_now_add=True)), ("actualizado_en", models.DateTimeField(auto_now=True)), ("espacio", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="reservas", to="reservas.espacio")), ("revisado_por", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="reservas_revisadas", to=settings.AUTH_USER_MODEL)), ("solicitante", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="reservas", to=settings.AUTH_USER_MODEL))], options={"ordering": ["-fecha", "hora_inicio"]}),
        migrations.AddIndex(model_name="reserva", index=models.Index(fields=["espacio", "fecha", "estado"], name="res_esp_fecha_estado_idx")),
    ]
