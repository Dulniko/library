from catalog.models import Author, Book, Publisher
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = "__all__"
