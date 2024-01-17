from django.contrib import admin

from catalog.models import Author, Book, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "popularity_score")
    search_fields = ("firstname", "lastname")
    list_filter = ("popularity_score", )
    raw_id_fields = ("recommendedby", "followers")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "price", "published_date")
    search_fields = ("title", "genre")
    list_filter = ("published_date", )
    raw_id_fields = ("author", "publisher")


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "popularity_score")
    search_fields = ("name", )
    list_filter = ("popularity_score", )
