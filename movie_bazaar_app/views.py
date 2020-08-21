from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


class HomeView(View):
    def get(self, request):
        movies = Movie.objects.all()
        ctx = {
            'movies': movies
        }
        return render(request, 'homepage.html', ctx)


class MovieDatailsView(View):

    def get(self, request, movie_id):
        movie = Movie.objects.get(pk=movie_id)
        movie_actors = movie.actor_set.all()
        ctx = {'movie': movie, 'movie_actors': movie_actors}
        # ctx['movie'] = get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movie_details.html', ctx)


class NewMovieView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'new-movie'

    def get(self, request):
        form = MovieForm()
        ctx = {"form": form}
        return render(request, "movie-form.html", ctx)

    def post(self, request):
        form = MovieForm(request.POST or None, request.FILES or None)
        ctx = {"form": form}

        if form.is_valid():
            form.save()
            return redirect('homepage')

        return render(request, "movie-form.html", ctx)


class EditMovieView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'edit-movie'

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        form = MovieForm(instance=movie)
        ctx = {"form": form,
               "movie": movie
               }
        return render(request, "movie-form.html", ctx)

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)  # sprawdzam czy obiekt istnieje i przypisuję go do zmiennej
        form = MovieForm(request.POST or None, request.FILES or None, instance=movie) #  wrzucamy do formularza instancję zmiennej movie
        ctx = {"form": form,
               "movie": movie
               }

        if form.is_valid():
            form.save()
            return redirect('homepage')

        return render(request, "movie-form.html", ctx)


class DeleteMovieView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'delete-movie'

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        ctx = {"movie": movie}
        return render(request, "delete.html", ctx)

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        ctx = {'movie': movie}

        if request.method == "POST":  # jeśli metoda jest POST to usuń film
            movie.delete()
            return redirect('homepage')

        return render(request, 'delete.html', ctx)