from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView,CreateView
# Create your views here.
class PublicacionListView(ListView):
    model=Publicacion
    fields='__all__'

class PublicacionCreateView(CreateView):
    model=Publicacion
    fields='__all__'
    success_url='/'