from django.forms import ModelForm
from .models import Movie, MovieRating


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'poster', 'actors', 'genre']


class MovieRateForm(ModelForm):
    class Meta:
        model = MovieRating
        fields = ['rate', 'review']
