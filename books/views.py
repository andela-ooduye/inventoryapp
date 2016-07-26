from django.shortcuts import render
from django.db.models import Q
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.order_by('-id')[:5]
    context = {'books' : books}
    return render(request, 'books/index.html', context)

def results(request):
    search = request.POST['search']

    try:
        advanced_search = request.POST['advanced_search']
        if advanced_search == 'title':
            books = Book.objects.raw("SELECT * FROM books_book WHERE title LIKE %s", [search])
        else:
            books = Book.objects.raw("SELECT * FROM books_book WHERE category LIKE %s", [search])

        context = {'books' : books}
        return render(request, 'books/index.html', context)

    except Exception:
        pass

    books = Book.objects.raw("SELECT * FROM books_book WHERE title LIKE %s OR category LIKE %s", [search, search])
    context = {'books' : books}
    return render(request, 'books/index.html', context)
