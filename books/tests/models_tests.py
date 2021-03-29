from django.test import TestCase, Client
from model_bakery import baker
from books.models import Author, Category, Book


class TestAuthorModel(TestCase):

    def test_create_author(self):

        # prepare
        author = Author(name="Tolkien")

        # make
        author.save()

        # check
        assert author.id == 1

    def test_create_author_with_null_name(self):

        # prepare
        author = Author()

        # make
        author.save()

        # check
        assert author.id == 1

class TestCategoryModel(TestCase):

    def test_create_category(self):

        # prepare
        category = Category(name="Tolkien")

        # make
        category.save()

        # check
        assert category.id == 1

    def test_create_category_with_null_name(self):

        # prepare
        category = Category()

        # make
        category.save()

        # check
        assert category.id == 1


class TestBookModel(TestCase):

    def setUp(self):
        authors_set = baker.prepare(Author, _quantity=5)
        self.book = baker.make(Book, authors=authors_set)

    def test_create_book(self):

        # prepare
        authors_amount = self.book.authors.count()

        # make
        self.book.save()

        # check
        assert self.book.id == 1
        assert authors_amount == 5


    def test_create_book_with(self):

        # prepare
        authors_amount = self.book.authors.count()

        # make
        self.book.save()

        # check
        assert self.book.id == 1
        assert authors_amount == 5

 