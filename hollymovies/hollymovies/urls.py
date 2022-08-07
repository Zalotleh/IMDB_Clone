"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from viewer.views import (hello,
                          movies,
                          ListMovies,
                          about,
                          CreateMovie,
                          DetailMovie,
                          UpdateMovie,
                          DeleteMovie,
                          ListActor,
                          CreateActor,
                          DetailActor,
                          UpdateActor,
                          DeleteActor,
                          ListDirector,
                          DetailDirector,
                          CreateDirector,
                          DeleteDirector,
                          UpdateDirector)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello_page'),
    path('movies/<s>', movies, name='movies_page'),
    path('about/', about, name='about'),

    path('', ListMovies.as_view(), name='home_page'),  # make it our home page
    path('title/<int:pk>', DetailMovie.as_view(), name='detail_movie'),
    path('create_movie/', CreateMovie.as_view(), name='create_movie'),
    path('title/<int:pk>/update', UpdateMovie.as_view(), name='update_movie'),
    path('title/<int:pk>/delete', DeleteMovie.as_view(), name='delete_movie'),
    path('actors_list/', ListActor.as_view(), name='actors_list'),
    path('name/<int:pk>', DetailActor.as_view(), name='detail_actor'),
    path('create_actor/', CreateActor.as_view(), name='create_actor'),
    path('name/<int:pk>/update', UpdateActor.as_view(), name='update_actor'),
    path('name/<int:pk>/delete', DeleteActor.as_view(), name='delete_actor'),
    path('director_list/', ListDirector.as_view(), name='directors_list'),
    path('name/<int:pk>', DetailDirector.as_view(), name='detail_director'),
    path('create_director/', CreateDirector.as_view(), name='create_director'),
    path('name/<int:pk>/update', UpdateDirector.as_view(), name='update_director'),
    path('name/<int:pk>/delete', DeleteDirector.as_view(), name='delete_director'),
]
