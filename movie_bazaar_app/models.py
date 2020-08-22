from django.db import models

GENRE = {
    (0, 'Inne'),
    (1, 'Horror'),
    (2, 'Komedia'),
    (3, 'Sci-fi'),
    (4, 'Dramat'),
    (5, 'Akcja'),
    (6, 'Katastroficzny'),
    (7, 'Animowany'),
    (8, 'Kryminalny'),
}

RATE = (
    (0, "☆☆☆☆☆☆☆☆☆☆"),
    (1, "★☆☆☆☆☆☆☆☆☆"),
    (2, "★★☆☆☆☆☆☆☆☆"),
    (3, "★★★☆☆☆☆☆☆☆"),
    (4, "★★★★☆☆☆☆☆☆"),
    (5, "★★★★★☆☆☆☆☆"),
    (6, "★★★★★★☆☆☆☆"),
    (7, "★★★★★★★☆☆☆"),
    (8, "★★★★★★★★☆☆"),
    (9, "★★★★★★★★★☆"),
    (10,"★★★★★★★★★★"),
)


class Movie(models.Model):
    title = models.CharField(max_length=250)
    actors = models.ManyToManyField("Actor", through="ActorMovie")
    genre = models.IntegerField(choices=GENRE, null=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    year = models.IntegerField(null=True)
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.title}"


class MovieRating(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, null=True)
    rate = models.IntegerField(choices=RATE)
    review = models.TextField(default="", blank=True)

    def __str__(self):
        return f"{self.get_rate_display()}"

# aby wyświetlis listę filmów Leonarda:
# movie =  Movie.objects.filter(actors__name="Leonardo DiCaprio")
# print(movie)
# lub
# actor = Actor.objects.get(name="Leonardo DiCaprio")
# movies = actor.movie_set.all()
# print(movies)


class Actor(models.Model):
    name = models.CharField(max_length=120)
    movies = models.ManyToManyField("Movie", through="ActorMovie")

    def __str__(self):
        return f"{self.name}"


class ActorMovie(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    actor = models.ForeignKey("Actor", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title}"


class ActorRating(models.Model):
    actor = models.ForeignKey("Actor", on_delete=models.CASCADE, null=True)
    rate = models.IntegerField(choices=RATE)
    review = models.TextField(default="", blank=True)

    def __str__(self):
        return f"{self.actor.name} {self.get_rate_display()}"