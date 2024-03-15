from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from catalog.serializers import (
    UserSerializer,
    AuthorSerializer,
    BookSerializer,
    PublisherSerializer,
)
from catalog.models import Author, Book, Publisher


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
