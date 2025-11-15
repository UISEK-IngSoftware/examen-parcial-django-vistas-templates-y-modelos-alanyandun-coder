from django.shortcuts import render, get_object_or_404
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all().order_by("title")
    context = {
        "movies": movies,
        "site_title": "Movie Library",
    }
    
    return render(request, "movies/movie_list.html", context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        "movie": movie,
        "site_title": "Movie Details",
    }
    
    return render(request, "movies/movie_detail.html", context)
