from django import forms

#Creamos las clases con los formularios pertenecientes
class ContactForm(forms.Form):
    #Atributos del formulario de contacto
    tipomsj = forms.CharField(label="Tipo de Petición", required=True)
    usuario = forms.CharField(label="Tu nombre", required=True) 
    correo = forms.EmailField(label="Correo Electrónico", required=True) 
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea) 
