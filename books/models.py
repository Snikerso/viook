from django.db import models



class IName(models.Model):
    name = models.CharField( max_length=50,null=True, blank=True) # translate
   
    def __str__(self):
        return f"Author: {self.name} "

    class Meta:
        abstract = True

class Author(IName):
   
    def __str__(self):
        return f"Author: {self.name} "

class Category(IName):
    
    def __str__(self):
        return f"Category: {self.name}"

class Book(models.Model):
    title = models.CharField( max_length=200, null=False, blank=False) # word
    authors = models.ManyToManyField(Author, related_name="authors") # translate
    categories = models.ManyToManyField(Category, related_name="categories") # example
    published_date = models.CharField( max_length=80, blank=True) # association
    avarage_rating = models.IntegerField( default=0, blank=True) # example
    ratings_count = models.IntegerField(default=0 ,blank=True)
    thumbnail = models.CharField(default="", max_length=300, blank=True)

    def __str__(self):
        return f"Book: {self.title} "