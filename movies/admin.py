from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "publication_year", "genre", "director_name", "synopsis")
    list_display_links = ("title",)
    search_fields = ("title", "director_name", "genre")
    list_filter = ("genre", "publication_year")
