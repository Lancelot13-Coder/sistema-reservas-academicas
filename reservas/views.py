from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import ReservaForm
from .models import Espacio, PerfilUsuario, Reserva

class LoginViewPersonalizada(LoginView):
    template_name = "registration/login.html"

@login_required
def cerrar_sesion(request):
    if request.method == "POST":
        logout(request)
    return redirect("login")

def es_gestor(user):
    if user.is_superuser or user.is_staff:
        return True
    perfil, _ = PerfilUsuario.objects.get_or_create(usuario=user)
    return perfil.rol == PerfilUsuario.Rol.GESTOR

@login_required
def inicio(request):
    mis_reservas = Reserva.objects.filter(solicitante=request.user).select_related("espacio")[:5]
    return render(request, "reservas/inicio.html", {"mis_reservas": mis_reservas, "espacios_activos": Espacio.objects.filter(activo=True).count()})

@login_required
def lista_espacios(request):
    espacios = Espacio.objects.filter(activo=True)
    return render(request, "reservas/espacios.html", {"espacios": espacios})

@login_required
def lista_reservas(request):
    if es_gestor(request.user):
        reservas = Reserva.objects.select_related("espacio", "solicitante", "revisado_por")
    else:
        reservas = Reserva.objects.filter(solicitante=request.user).select_related("espacio")
    return render(request, "reservas/lista_reservas.html", {"reservas": reservas, "es_gestor": es_gestor(request.user)})

@login_required
def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    reserva = form.save(commit=False)
                    reserva.solicitante = request.user
                    reserva.save()
                messages.success(request, "Solicitud de reserva creada y enviada para revisión.")
                return redirect("detalle_reserva", pk=reserva.pk)
            except Exception as exc:
                # ValidationError from model-level checks is surfaced as a form error.
                from django.core.exceptions import ValidationError
                if isinstance(exc, ValidationError):
                    form.add_error(None, exc)
                else:
                    raise
    else:
        form = ReservaForm()
    return render(request, "reservas/form_reserva.html", {"form": form})

@login_required
def detalle_reserva(request, pk):
    reserva = get_object_or_404(Reserva.objects.select_related("espacio", "solicitante", "revisado_por"), pk=pk)
    if reserva.solicitante_id != request.user.id and not es_gestor(request.user):
        return HttpResponseForbidden("No tienes permiso para consultar esta reserva.")
    return render(request, "reservas/detalle_reserva.html", {"reserva": reserva, "puede_gestionar": es_gestor(request.user)})

@login_required
@require_POST
def aprobar_reserva(request, pk):
    if not es_gestor(request.user):
        return HttpResponseForbidden("Solo un gestor puede aprobar reservas.")
    with transaction.atomic():
        reserva = get_object_or_404(Reserva.objects.select_for_update(), pk=pk)
        if reserva.estado != Reserva.Estado.PENDIENTE:
            messages.error(request, "Solo se pueden aprobar reservas pendientes.")
        else:
            # Revalidar conflictos antes de aprobar.
            reserva.estado = Reserva.Estado.APROBADA
            reserva.revisado_por = request.user
            try:
                reserva.save()
                messages.success(request, "Reserva aprobada.")
            except Exception as exc:
                from django.core.exceptions import ValidationError
                if isinstance(exc, ValidationError):
                    reserva.estado = Reserva.Estado.PENDIENTE
                    messages.error(request, "No se pudo aprobar: existe un conflicto de horario.")
                else:
                    raise
    return redirect("detalle_reserva", pk=pk)

@login_required
@require_POST
def rechazar_reserva(request, pk):
    if not es_gestor(request.user):
        return HttpResponseForbidden("Solo un gestor puede rechazar reservas.")
    reserva = get_object_or_404(Reserva, pk=pk)
    if reserva.estado != Reserva.Estado.PENDIENTE:
        messages.error(request, "Solo se pueden rechazar reservas pendientes.")
    else:
        reserva.estado = Reserva.Estado.RECHAZADA
        reserva.revisado_por = request.user
        reserva.observaciones = request.POST.get("observaciones", "").strip()[:2000]
        reserva.save()
        messages.success(request, "Reserva rechazada.")
    return redirect("detalle_reserva", pk=pk)

@login_required
@require_POST
def cancelar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if reserva.solicitante_id != request.user.id and not es_gestor(request.user):
        return HttpResponseForbidden("No tienes permiso para cancelar esta reserva.")
    if reserva.estado not in [Reserva.Estado.PENDIENTE, Reserva.Estado.APROBADA]:
        messages.error(request, "Solo se pueden cancelar reservas pendientes o aprobadas.")
    else:
        reserva.estado = Reserva.Estado.CANCELADA
        reserva.save()
        messages.success(request, "Reserva cancelada.")
    return redirect("detalle_reserva", pk=pk)
