from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
import requests
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django.http import Http404


class BookFilter(django_filters.FilterSet):

    author = django_filters.CharFilter(
        field_name='authors__name',
        lookup_expr='contains',
    )
    sort = django_filters.OrderingFilter(
        fields=(
            ('published_date','published_date')
        ),
    )

    class Meta:
        model = Book
        fields = ("author","published_date","sort")
        
class  BooksListView(generics.ListAPIView):
    queryset = Book.objects.prefetch_related("authors","categories")
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    

class BoookViewDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise  Response({"Fail": "Nie ma takiej książki"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostBooks(APIView):

    def post(self, request):

        url = f'https://www.googleapis.com/books/v1/volumes?q={request.data["q"]}' 
        response = requests.get(url)
        data = response.json()
        data_items = data.get("items")

        if data_items == None: return Response("Nie ma takich książek", status=status.HTTP_400_BAD_REQUEST)

        books = [{
            "title":i["volumeInfo"]["title"],
            "authors":i["volumeInfo"].get("authors") if i["volumeInfo"].get("authors") else [],
            "categories":i["volumeInfo"].get("categories") if i["volumeInfo"].get("categories") else [],
            "published_date":i["volumeInfo"].get("publishedDate") if i["volumeInfo"].get("publishedDate") else "0000",
            "avarage_rating":i["volumeInfo"].get("averageRating") if i["volumeInfo"].get("averageRating") else 0,
            "ratings_count":i["volumeInfo"].get("ratingsCount") if i["volumeInfo"].get("ratingsCount") else 0,
            "thumbnail":i["volumeInfo"]["imageLinks"].get("thumbnail") if i["volumeInfo"]["imageLinks"].get("thumbnail") else "",
        } for i in data_items]

        serializer = BookSerializer(data=books, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)