from django import forms
from .models import Movie, MovieRating, Actor


class MovieSearchForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'poster', 'actors', 'genre']


class MovieRateForm(forms.ModelForm):
    class Meta:
        model = MovieRating
        fields = ['rate', 'review']


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'movies']
