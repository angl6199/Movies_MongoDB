from typing import ClassVar
from django.shortcuts import render
from django.views.generic import *
from .models import Movies

# Create your views here.
class ViewEjemplos(ListView):

    def get(self, request, *args, **kwargs):
        objetos = Movies.objects.all()
        query = Movies.objects.filter(name="Angel")
        return render(request, "users_manager.html", {'movies': objetos})

class ViewMain(TemplateView):
    template_name = "part_one.html"
