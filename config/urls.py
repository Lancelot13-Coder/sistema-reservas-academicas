from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("accounts/login/", views.LoginViewPersonalizada.as_view(), name="login"),
    path("accounts/logout/", views.cerrar_sesion, name="logout"),
    path("espacios/", views.lista_espacios, name="espacios"),
    path("reservas/", views.lista_reservas, name="reservas"),
    path("reservas/nueva/", views.crear_reserva, name="crear_reserva"),
    path("reservas/<int:pk>/", views.detalle_reserva, name="detalle_reserva"),
    path("reservas/<int:pk>/aprobar/", views.aprobar_reserva, name="aprobar_reserva"),
    path("reservas/<int:pk>/rechazar/", views.rechazar_reserva, name="rechazar_reserva"),
    path("reservas/<int:pk>/cancelar/", views.cancelar_reserva, name="cancelar_reserva"),
]
