from django import forms
from django.utils import timezone
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["espacio", "fecha", "hora_inicio", "hora_fin", "motivo"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "hora_inicio": forms.TimeInput(attrs={"type": "time"}),
            "hora_fin": forms.TimeInput(attrs={"type": "time"}),
            "motivo": forms.TextInput(attrs={"maxlength": 250, "placeholder": "Motivo académico de la reserva"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["espacio"].queryset = self.fields["espacio"].queryset.filter(activo=True)
        self.fields["fecha"].widget.attrs["min"] = timezone.localdate().isoformat()
