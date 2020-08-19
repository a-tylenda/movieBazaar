from django.contrib import admin
from .models import Movie, Actor, ActorMovie, MovieRating, ActorRating

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(ActorMovie)
admin.site.register(MovieRating)
admin.site.register(ActorRating)



