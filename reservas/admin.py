from django.contrib import admin
from .models import Espacio, PerfilUsuario, Reserva

@admin.register(Espacio)
class EspacioAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "ubicacion", "capacidad", "activo")
    list_filter = ("activo",)
    search_fields = ("codigo", "nombre", "ubicacion")

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "rol")
    list_filter = ("rol",)
    search_fields = ("usuario__username", "usuario__email")

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id", "espacio", "solicitante", "fecha", "hora_inicio", "hora_fin", "estado")
    list_filter = ("estado", "fecha", "espacio")
    search_fields = ("espacio__nombre", "solicitante__username", "motivo")
    readonly_fields = ("creado_en", "actualizado_en")
