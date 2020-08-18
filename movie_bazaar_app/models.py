from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(default="")
    director = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="directed_by", default="")
    screenplay = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="screenplay_by", default="")
    starring = models.ManyToManyField("Person", through="PersonMovie")
    premiere = models.DateField(null=True, blank=True)
    production = models.CharField(max_length=120, default="")
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Person(models.Model):
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PersonMovie(models.Model):
    ROLES = {
        (1, 'director'),
        (2, 'screenplay'),
        (3, 'actor'),
        (4, 'actress')
    }
    role = models.IntegerField(choices=ROLES, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.role} {self.person} {self.movie}"


class Rate(models.Model):
    RATING = (
        (0, "☆☆☆☆☆"),
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    )
    review = models.TextField(default="", blank=True)
    rating = models.IntegerField(choices=RATING)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} {self.get_rating_display()}"


class AdditionalInfo(models.Model):
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

    duration = models.PositiveSmallIntegerField(default=0)
    genre = models.PositiveSmallIntegerField(choices=GENRE, default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} (czas:{self.duration}min, {self.get_genre_display()})"