from rest_framework import serializers
from .models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name']

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        author = {
            "name": data
        }
        return author


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        category = {
            "name": data
        }
        return category


class BookSerializer(serializers.ModelSerializer):

    authors = AuthorSerializer(many=True)
    categories = CategorySerializer(many=True)

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        categories = validated_data.pop('categories')
        keep_authors = [ Author.objects.get_or_create(**i)[0] for i in authors]
        keep_categories = [ Category.objects.get_or_create(**i)[0] for i in categories]
        
        
        book = Book.objects.get_or_create( **validated_data)[0]
        book.authors.set(keep_authors)
        book.categories.set(keep_categories)
        book.save()
        return book
        

    class Meta:
        model = Book
        fields = ['id','title','authors',"published_date","categories","avarage_rating","ratings_count","thumbnail"]


