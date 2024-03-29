from django.urls import path, include
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/",
         SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger"),
    path("redoc/",
         SpectacularRedocView.as_view(url_name="schema"),
         name="redoc"),
]
