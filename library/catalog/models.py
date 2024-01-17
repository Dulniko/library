from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    recommendedby = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="recommended_authors",
        related_query_name="recommended_authors",
        null=True,
        blank=True,
    )
    joindate = models.DateField()
    popularity_score = models.IntegerField(blank=True, null=True)
    followers = models.ManyToManyField(User,
                                       related_name="followed_authors",
                                       related_query_name="followed_authors",
                                       blank=True)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    published_date = models.DateField()
    author = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="books",
        related_query_name="books",
    )
    publisher = models.ForeignKey(
        "Publisher",
        on_delete=models.CASCADE,
        related_name="books",
        related_query_name="books",
    )

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    joindate = models.DateField()
    popularity_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
