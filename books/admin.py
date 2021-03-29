from django.contrib import admin
from .models import Book, Author,Category


class BookAdmin(admin.ModelAdmin):
    list_display = ("id","title",)
    list_filter = ("title",)

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Category)