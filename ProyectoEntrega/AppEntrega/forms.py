from django import forms

class TecnicosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    edificio = forms.CharField(max_length=30)
    
class UsuariosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    legajo = forms.CharField(max_length=20)

class TicketFormulario(forms.Form):
    numero = forms.IntegerField()
    estado = forms.BooleanField()