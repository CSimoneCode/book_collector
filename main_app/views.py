from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

### ------- Static pages
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


### ------- Book views
def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def books_show(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/show.html', {'book': book})


def books_new(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            new_book = book_form.save(commit=False)
            new_book.save()

            return redirect('books_show', new_book.id)
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'books/new.html', context)

def books_edit(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        book_form = BookForm(request.POST, instance=book)
        if book_form.is_valid():
            updated_book = book_form.save()
            return redirect('books_show', updated_book.id)
    else:
        form = BookForm(instance=book)
        context ={'form': form ,'book': book}
        return render(request, 'books/edit.html', context)
