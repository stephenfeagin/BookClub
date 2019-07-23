from django.urls import path

from . import views


urlpatterns = [
    path("authors/", views.AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
    path("books/", views.BookListView.as_view(), name="book-list"),
    path("books/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    path("genres/", views.GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>", views.GenreDetailView.as_view(), name="genre-detail"),
]
