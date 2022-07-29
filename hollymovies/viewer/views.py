from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

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


def database_movies(request):
    movies_data = Movie.objects.all()
    context = {
        'movies_data': movies_data
    }
    return render(request, 'movies.html', context=context)
