from django.test import TestCase
from .models import Book
from django.core.urlresolvers import reverse

# Create your tests here.

def create_book(title, category, short_description):
    '''
    Creates a new book instance into the test datbase
    '''
    return Book.objects.create(title=title, category=category, short_description=short_description)

class BookTest(TestCase):

    def test_string_representation(self):
        book = Book(title="Harry Potter")
        self.assertEqual(str(book), 'Book object')

class BookViewTests(TestCase):

    def test_index_view_with_no_books(self):
        """
        If no books exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('books:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no books.")
        self.assertQuerysetEqual(response.context['books'], [])

    def test_index_view_with_two_books(self):
        """
        The books index page may display multiple books.
        """
        create_book('Harry Potter', 'Fiction', 'A J.K Rowling book')
        create_book('Things Fall Apart', 'Non-fiction', 'A Wole Soyinka book')
        response = self.client.get(reverse('books:index'))
        self.assertQuerysetEqual(
            response.context['books'],
            ['<Book: Book object>', '<Book: Book object>']
        )
