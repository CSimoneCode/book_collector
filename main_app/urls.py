from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # static routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # book routes
    path('books/', views.books_index, name='books_index'),
    path('books/new', views.books_new, name='books_new'),
    path('books/<int:book_id>/', views.books_show, name='books_show'),
    path('books/<int:book_id>/edit', views.books_edit, name='books_edit')
]
    