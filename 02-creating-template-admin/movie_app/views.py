from django.shortcuts import render


def index(request):
    return render(request, "movie_app/movie_app_home.html")
