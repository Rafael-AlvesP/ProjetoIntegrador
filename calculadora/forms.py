# forms.py
from django import forms
from .models import Prazo

class PrazoForm(forms.ModelForm):
    class Meta:
        model = Prazo
        fields = ['nomeEvento', 'processo', 'evento', 'dataPubli', 'prazoDias', 'notificar']
