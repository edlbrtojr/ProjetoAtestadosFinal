from django import forms
from .models import Atestado
from django.forms import Form, ModelForm, DateField, widgets

class AtestadoForm(forms.ModelForm):
    class Meta:
        model = Atestado
        fields = '__all__'
        widgets = {
            "data_atestado" : widgets.DateInput(attrs={'type':'date'})
        }

class AtestadoFilterForm(forms.Form):
    nome_aluno = forms.CharField(required=False)
    data_afastamento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    turma_aluno = forms.CharField(required=False)
    ano_aluno = forms.CharField(required=False)
