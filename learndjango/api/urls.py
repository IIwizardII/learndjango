from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BooksListCreate.as_view(), name="books_view_create")
]