"""movieBazaar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from movie_bazaar_app.views import HomeView, MovieDatailsView, NewMovieView, EditMovieView, DeleteMovieView, \
    MovieSearch, NewActorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'), # html jest w templates/registration (zgodnie z dokumentacją dj)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='homepage'),
    path('movie-search', MovieSearch.as_view(), name='movie-search'),
    path('movie-details/<int:movie_id>/', MovieDatailsView.as_view(), name='movie-details'),
    path('new-movie/', NewMovieView.as_view(), name='new-movie'),
    path('new-actor/', NewActorView.as_view(), name='new-actor'),
    path('edit-movie/<int:movie_id>/', EditMovieView.as_view(), name='edit-movie'),
    path('delete-movie/<int:movie_id>/', DeleteMovieView.as_view(), name='delete-movie'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
