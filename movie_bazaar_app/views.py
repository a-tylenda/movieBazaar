from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, CreateView, DeleteView
from .models import Movie, ActorMovie, MovieRating
from .forms import MovieForm, MovieRateForm, MovieSearchForm
from django.db.models import Avg


class HomeView(View):
    def get(self, request):
        movies = Movie.objects.all()
        ctx = {
            'movies': movies
        }
        return render(request, 'homepage.html', ctx)


class MovieSearch(TemplateView):
    template_name = 'movie-search.html'

    def get_context_data(self, **kwargs):
        if self.request.GET:
            form = MovieSearchForm(self.request.GET)
            if form.is_valid():
                movies = Movie.objects.filter(title__icontains=form.cleaned_data['title'])
            else:
                movies = []
        else:
            form = MovieSearchForm()
            movies = None
        ctx = {"form": form,
               "movies": movies}
        return ctx


class MovieDatailsView(View):

    def get(self, request, movie_id):
        ctx = {}
        movie = get_object_or_404(Movie, pk=movie_id)
        ctx['movie'] = movie
        ctx['movie_actors'] = movie.actor_set.all()
        ratings = MovieRating.objects.filter(movie__id=movie_id)
        ctx['ratings'] = ratings
        ctx['all_ratings'] = MovieRating.objects.filter(movie__id=movie_id).count()
        avg_rating = ratings.aggregate(Avg('rate'))['rate__avg']
        ctx['avg_rating'] = avg_rating
        ctx['form'] = MovieRateForm()

        return render(request, 'movie_details.html', ctx)

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        ratings = MovieRating.objects.filter(movie__id=movie_id)
        form = MovieRateForm(request.POST or None)
        ctx = {"movie": movie, "ratings": ratings, "form": form}

        if request.method == 'POST':
            if 'rate' in request.POST:
                rate = form.save(commit=False)  # daję commit=Flase, bo chcę przypisać ocenę do filmu zanim wyślę do bazy
                rate.movie = movie
                rate.save()

        return render(request, "movie_details.html", ctx)


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
        ctx = {"movie": movie, "form": form}
        return render(request, "movie-form.html", ctx)

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)  # sprawdzam czy obiekt istnieje i przypisuję go do zmiennej
        form = MovieForm(request.POST or None, request.FILES or None, instance=movie) #  wrzucamy do formularza instancję zmiennej movie
        ctx = {"movie": movie, "form": form}

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


# class RatingView(View):
#     def get(self, request, movie_id):
#
# class RatingView(View):
#     def get(self, request, movie_id):
#         movie = get_object_or_404(Movie, pk=movie_id)
#         rates = MovieRating.objects.filter(movie__id=movie_id)
#         form = MovieRateForm()
#         ctx = {"movie": movie, "form": form, "rates": rates}
#         return render(request, "movie_details.html", ctx)
#
#     def post(self, request, movie_id):
#         movie = get_object_or_404(Movie, pk=movie_id)
#         rates = MovieRating.objects.filter(movie__id=movie_id)
#         form = MovieRateForm(request.POST or None)
#         ctx = {"movie": movie, "form": form, "rates": rates}
#
#         if request.method == 'POST':
#             if 'rate' in request.POST:
#                 rate = form.save(commit=False)  # daję commit=Flase, bo chcę przypisać ocenę do filmu zanim wyślę do bazy
#                 rate.movie = movie
#                 rate.save()
#
#         return render(request, "movie_details.html", ctx)