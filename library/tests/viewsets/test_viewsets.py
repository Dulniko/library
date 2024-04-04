import pytest
from django.urls import reverse
from rest_framework import status
from tests.helpers import load_fixture
# from django.contrib.auth.models import User


@pytest.mark.django_db
@load_fixture(("tests/fixtures/authors.yaml", ))
def test_author_list(api_client):
    url = reverse("author-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == [
        {
            "id": 1,
            "firstname": "Andrzej",
            "lastname": "Sapkowski",
            "alive": True,
            "address": "Łódź",
            "zipcode": "90-008",
            "telephone": "123123123",
            "recommendedby": None,
            "joindate": "2024-01-20",
            "popularity_score": 80,
            "followers": [],
        },
        {
            "id": 2,
            "firstname": "Stephen",
            "lastname": "King",
            "alive": False,
            "address": "Broadway",
            "zipcode": "04401",
            "telephone": "213213213",
            "recommendedby": None,
            "joindate": "2024-01-19",
            "popularity_score": 77,
            "followers": [],
        },
    ]


@pytest.mark.django_db
@load_fixture(("tests/fixtures/authors.yaml", ))
def test_author_detail(api_client):
    url = reverse("author-detail", kwargs={"pk": 1})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": 1,
        "firstname": "Andrzej",
        "lastname": "Sapkowski",
        "alive": True,
        "address": "Łódź",
        "zipcode": "90-008",
        "telephone": "123123123",
        "recommendedby": None,
        "joindate": "2024-01-20",
        "popularity_score": 80,
        "followers": [],
    }