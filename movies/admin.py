from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'genre', 'release_date']
    search_fields = ['title', 'genre__name']
    list_filter = ['release_date', 'genre']
    ordering = ['-release_date']
