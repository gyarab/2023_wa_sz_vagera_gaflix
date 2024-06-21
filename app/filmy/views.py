from django.shortcuts import render
from filmy.models import Movie

def movies(request):
    context = {
        "movies": Movie.objects.all().order_by('name')
    }
    return render(request, "filmy/movies.html", context)


def movie(request, id):
    m = Movie.objects.get(id=id)

    context = {
        "movie": m,
    }
    return render(request, "filmy/movie.html", context)