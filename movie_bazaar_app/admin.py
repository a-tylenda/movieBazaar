from django.contrib import admin
from .models import Movie, Person, PersonMovie, Rate, AdditionalInfo

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(PersonMovie)
admin.site.register(Rate)
admin.site.register(AdditionalInfo)


