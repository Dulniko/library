from django.urls import path, include
from catalog.viewsets import UserViewSet, AuthorViewSet, BookViewSet, PublisherViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"authors", AuthorViewSet, basename="author")
router.register(r"books", BookViewSet, basename="book")
router.register(r"publishers", PublisherViewSet, basename="publisher")

urlpatterns = [
    path("", include(router.urls)),
]
