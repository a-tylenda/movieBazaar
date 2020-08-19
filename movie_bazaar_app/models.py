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
    (0, "☆☆☆☆☆"),
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


class Movie(models.Model):
    title = models.CharField(max_length=250)
    actors = models.ManyToManyField("Actor", through="ActorMovie")
    genre = models.IntegerField(choices=GENRE, null=True)

    def __str__(self):
        return f"{self.title}"


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


class MovieRating(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, null=True)
    rate = models.IntegerField(choices=RATE)
    review = models.TextField(default="", blank=True)


class ActorRating(models.Model):
    actor = models.ForeignKey("Actor", on_delete=models.CASCADE, null=True)
    rate = models.IntegerField(choices=RATE)
    review = models.TextField(default="", blank=True)