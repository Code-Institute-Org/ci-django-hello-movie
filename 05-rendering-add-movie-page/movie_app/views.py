from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.all()

    context = {
        "movies": movies,
    }
    return render(request, "movie_app/movie_app_home.html", context)


def add_movie(request):
    if request.method == "POST":
        form_data = {
            "title": request.POST["title"],
            "director": request.POST["director"],
            "genre": request.POST["genre"],
            "summary": request.POST["summary"],
            "rating": request.POST["rating"],
            "watched": "watched" in request.POST,
        }
        Movie.objects.create(**form_data)

    return render(request, "movie_app/movie_app_add.html")
