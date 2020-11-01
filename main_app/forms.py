from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'synopsis', 'word_count', 'year_published', 'genre', 'isbn')
    