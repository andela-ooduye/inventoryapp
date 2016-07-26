from django.shortcuts import render
from django.db.models import Q
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.order_by('id')[:5]
    context = {'books' : books}
    return render(request, 'books/index.html', context)

def results(request):
    search = request.POST['search']
    #     skills contain search  OR  title contains search
    #   query = Q(title=search ) | Q(category=search )
    books = Book.objects.raw("SELECT * FROM books_book WHERE title LIKE %s OR category LIKE %s", [search, search])
    context = {'books' : books}
    return render(request, 'books/index.html', context)
