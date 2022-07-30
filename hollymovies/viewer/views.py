from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.views.generic import ListView, CreateView, DetailView

movies_database = {
    'topgun': 'Top Gun is awesome',
    'thor': 'Thor is incredible'
}


def hello(request):
    return HttpResponse("hello Django!!!")


def movies(request, s):
    client_data = request.GET
    name = client_data.get('name')  # get() it will return the value from condition,
    # if it doesn't have the value it will show none, and doesn't get an error

    movies = Movie.objects.all()
    print(movies)

    if s in movies_database:
        info = movies_database[s]
        if name is None:
            return HttpResponse(info)
        return HttpResponse(f'hello {name}, {info}')
    else:
        return HttpResponse('movie not found')


# def database_movies(request):
#     movies_data = Movie.objects.all()
#     context = {
#         'movies_data': movies_data
#     }
#     return render(request, 'movies.html', context=context)


def about(request):
    movies_data = Movie.objects.all()
    total_movies = movies_data.count()
    context = {
        'total_movies': total_movies
    }
    return render(request, 'about.html', context=context)


# I left the above functions to compare them with the class based views CBV

class ListMovies(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies_data'


class CreateMovie(CreateView):
    template_name = 'create_movie.html'
    model = Movie
    success_url = '/'
    fields = '__all__'


class DetailMovie(DetailView):
    template_name = 'detail_movie.html'
    model = Movie
    context_object_name = 'movie'

