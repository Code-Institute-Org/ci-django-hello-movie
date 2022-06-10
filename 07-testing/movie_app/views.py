from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


def index(request):
    movies = Movie.objects.all()

    context = {
        "movies": movies,
    }
    return render(request, "movie_app/movie_app_home.html", context)


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = MovieForm()
    context = {
        "form": form,
    }
    return render(request, "movie_app/movie_app_add.html", context)


def edit_movie(request, id):
    movie = Movie.objects.get(pk=id)

    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = MovieForm(instance=movie)
    context = {
        "form": form,
        "movie": movie,
    }
    return render(request, "movie_app/movie_app_edit.html", context)


def toggle_movie(request, id):

    movie = Movie.objects.get(pk=id)
    movie.watched = not movie.watched
    movie.save()

    return redirect("index")


def delete_movie(request, id):

    movie = Movie.objects.get(pk=id)
    movie.delete()

    return redirect("index")
