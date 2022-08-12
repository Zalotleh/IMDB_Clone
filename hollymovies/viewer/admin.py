from django.contrib import admin
from .models import Movie, Director, Actor, Profile

# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Profile)
