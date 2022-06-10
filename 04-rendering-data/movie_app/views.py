from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.all()

    context = {
        "movies": movies,
    }
    return render(request, "movie_app/movie_app_home.html", context)
