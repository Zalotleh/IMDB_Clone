from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContactForm
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView,
                                  FormView
                                  )

from .constants import COUNTRIES_CHOICES
from .models import Movie, Actor, Director

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
    # success_url = reverse_lazy('home_page')
    fields = '__all__'

    # after updating the user will go back to the detail_movie page instead of home_page.
    def get_success_url(self):
        movie_pk = self.kwargs['pk']
        url = reverse_lazy('detail_movie', kwargs={'pk': movie_pk})
        return url


class DeleteMovie(DeleteView):
    template_name = 'delete_movie.html'
    model = Movie
    success_url = reverse_lazy('home_page')
    context_object_name = 'movie'


class DetailMovie(DetailView):
    template_name = 'detail_movie.html'
    model = Movie
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = context['movie'].country_of_origin
        country_name = get_country_name(country_code)

        context['country_name'] = country_name

        return context


# Below is the CRUD Operations for Actor model:

class ListActor(ListView):
    template_name = 'actors.html'
    model = Actor
    context_object_name = 'actor_data'


class CreateActor(CreateView):
    template_name = 'create_actor.html'
    model = Actor
    success_url = '/'
    fields = '__all__'


class UpdateActor(UpdateView):
    template_name = 'update_actor.html'
    model = Actor
    # success_url = reverse_lazy('actors_list')
    fields = '__all__'

    # after updating the user will go back to the detail_actor page instead of actor_list.
    def get_success_url(self):
        actor_pk = self.kwargs['pk']
        url = reverse_lazy('detail_actor', kwargs={'pk': actor_pk})
        return url


class DeleteActor(DeleteView):
    template_name = 'delete_actor.html'
    model = Actor
    success_url = reverse_lazy('actors_list')
    context_object_name = 'actor'


class DetailActor(DetailView):
    template_name = 'detail_actor.html'
    model = Actor
    context_object_name = 'actor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = context['actor'].country_of_birth
        country_name = get_country_name(country_code)
        context['country_name'] = country_name

        return context


# Below is the CRUD Operations for Director model:

class ListDirector(ListView):
    template_name = 'directors.html'
    model = Director
    context_object_name = 'director_data'


class CreateDirector(CreateView):
    template_name = 'create_director.html'
    model = Director
    success_url = '/'
    fields = '__all__'


class UpdateDirector(UpdateView):
    template_name = 'update_director.html'
    model = Actor
    # success_url = reverse_lazy('directors_list')
    fields = '__all__'

    # after updating the user will go back to the detail_movie page instead of director_list.
    def get_success_url(self):
        director_pk = self.kwargs['pk']
        url = reverse_lazy('detail_director', kwargs={'pk': director_pk})
        return url


class DeleteDirector(DeleteView):
    template_name = 'delete_director.html'
    model = Director
    success_url = reverse_lazy('directors_list')
    context_object_name = 'director'


class DetailDirector(DetailView):
    template_name = 'detail_director.html'
    model = Director
    context_object_name = 'director'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = context['director'].country_of_birth
        country_name = get_country_name(country_code)
        context['country_name'] = country_name

        return context


# class ContactPage(TemplateView):
#     template_name = 'contact.html'


class ContactPage(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        print('I received your contact')
        print(form.cleaned_data)
        # the form parameter has all the data we receive from the users, from here we can
        # manipulate it
        # for ex, if we want to send an email response, save some data in db, send telegram message, sms
        return super().form_valid(form)
