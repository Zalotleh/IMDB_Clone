from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  )

from django.urls import reverse_lazy
from .constants import COUNTRIES_CHOICES

movies_database = {
    'topgun': 'Top Gun is awesome',
    'thor': 'Thor is incredible'
}


def get_country_name(country_code):
    for country in COUNTRIES_CHOICES:
        if country[0] == country_code:
            return country[1]


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


# below is the CRUD operations for Movie model

class ListMovies(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies_data'


class CreateMovie(CreateView):
    template_name = 'create_movie.html'
    model = Movie
    success_url = '/'
    fields = '__all__'


class UpdateMovie(UpdateView):
    template_name = 'update_movie.html'
    model = Movie
    success_url = reverse_lazy('detail_movie')
    fields = '__all__'


class DeleteMovie(DeleteView):
    template_name = 'delete_movie.html'
    model = Movie
    success_url = reverse_lazy('home_page')
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = context['movie'].country_of_origin
        country_name = get_country_name(country_code)

        context['country_name'] = country_name

        return context


class DetailMovie(DetailView):
    template_name = 'detail_movie.html'
    model = Movie
    context_object_name = 'movie'
