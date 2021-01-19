from django import forms
from .models import Medicos

class MedicosForm(forms.ModelForm):

    class Meta:
        model = Medicos
        fields = '__all__'
        labels = {
            "nombre_medico": "Nombre",
            "jvpm": "Codigo JVPM" ,
            "fecha_nacimiento": "Fecha de Nacimiento",
            "especialidad": "Especialidad"
        }

    def __init__(self, *args, **kwargs):
        super(MedicosForm, self).__init__(*args, **kwargs)
        self.fields['especialidad'].empty_label = "Seleccione"
        self.fields['fecha_nacimiento'].required = False