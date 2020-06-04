from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse
from .forms import ContactForm

# Create your views here.

class  HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tituloIni':'Los saluda Daniela'})

class NosotrosPageView(TemplateView):
    
    template_name = "nosotros.html"

    def get_context_data(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tituloUs':'Los saluda Daniela'})

def contacto(request):
    FormContact = ContactForm()
    return render(request, 'contacto.html', {'formulario':FormContact})