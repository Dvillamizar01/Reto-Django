from django import forms  
from paciente.models import paciente  
class pacienteForm(forms.ModelForm):  
    class Meta:  
        model = paciente  
        fields = "__all__" 