from django.core.validators import RegexValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=
    "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)
zipcode_regex = RegexValidator(
    regex=r'^\d{5}$', message="Zip code must be composed of 5 digits.")


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    alive = models.BooleanField()
    address = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=5,
                               validators=[zipcode_regex],
                               null=True,
                               blank=True)
    telephone = models.CharField(unique=True,
                                 null=True,
                                 blank=True,
                                 validators=[phone_regex])
    recommendedby = models.ForeignKey("self",
                                      on_delete=models.CASCADE,
                                      related_name="recommended_authors",
                                      null=True,
                                      blank=True)
    joindate = models.DateField(
        validators=[MaxValueValidator(limit_value=timezone.now)])
    popularity_score = models.PositiveIntegerField(blank=True, null=True)
    followers = models.ManyToManyField(User,
                                       related_name="followed_authors",
                                       blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    published_date = models.DateField()
    author = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="books",
    )
    publisher = models.ForeignKey(
        "Publisher",
        on_delete=models.CASCADE,
        related_name="books",
    )

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    joindate = models.DateField()
    popularity_score = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
