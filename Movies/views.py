from typing import ClassVar
from django.shortcuts import render
from django.views.generic import *
from .models import Movies
from django.db.models import Q

# Create your views here.
class ViewSearch(ListView):

    def get(self, request, value, *args, **kwargs):
        field = request.GET.get('search-fields')
        search_input = request.GET.get('search-input')
        count = 0
        all = False
        if(search_input!=None and field!="Choose one..."):
            if field=="Movie name":
                movies = Movies.objects.filter(Q(title__icontains = search_input) & Q(type = "Movie"))
                shows = None
            if field=="Actor":
                movies = Movies.objects.filter(Q(cast__icontains = search_input) & Q(type = "Movie"))
                shows = Movies.objects.filter(Q(cast__icontains = search_input) & Q(type = "TV Show"))
            if field=="TV show":
                movies = None
                shows = Movies.objects.filter(Q(title__icontains = search_input) & Q(type = "TV Show"))
        elif (value == 1):
                all = True
                movies = Movies.objects.all()
                shows = None
        else:
            movies = "No movies"
            count = Movies.objects.all().count()
            shows = None
        
        return render(request, "search_movies.html", {'movies': movies, 'category': field, 'searched_input': search_input, 'shows': shows, 'count':count, 'all':all})

class ViewStatistics(TemplateView):
    def get(self, request, *args, **kwargs):
        field = request.GET.get('search-fields')
        search_input = request.GET.get('search-input')

        if(search_input!=None and field!="Choose one..."):
            if field=="Country":
                validar = Movies.objects.filter(Q(country__icontains = search_input) & Q(type = "Movie")).exists()
                n1 = Movies.objects.filter(Q(country__icontains = search_input) & Q(type = "Movie")).count()
                n2 = Movies.objects.filter(Q(type = "Movie")).count() - n1
                l1 = search_input
                l2 = "Other countries"
            if field=="Release year":
                search_input = search_input 
                validar = Movies.objects.filter(Q(release_year__icontains = search_input) & Q(type = "TV Show")).exists()
                n1 = Movies.objects.filter(Q(release_year__icontains = search_input) & Q(type = "TV Show")).count()
                n2 = Movies.objects.filter(Q(type = "TV Show")).count() - n1
                l1 = search_input
                l2 = "Other years"
        else:
            validar = True
            n1 = Movies.objects.filter(Q(type = "Movie")).count()
            n2 = Movies.objects.filter(Q(type = "TV Show")).count()
            l1 = "Movies"
            l2 = "TV Shows"

        return render(request, "statistics.html", {"n1":n1, "n2":n2, "l1":l1, "l2":l2, "category":field, 'searched_input': search_input, 'validar':validar})

class ViewMain(TemplateView):
    template_name = "part_one.html"
