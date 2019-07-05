from django.contrib import admin

from .models import Author, Book, Genre


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
