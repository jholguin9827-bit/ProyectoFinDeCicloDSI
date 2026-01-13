from django import forms
from .models import Estudiante, Docente, Periodo, Curso, Inscripcion

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
