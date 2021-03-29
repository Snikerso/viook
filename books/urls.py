from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import BooksListView, BoookViewDetail, PostBooks

router = routers.DefaultRouter()

urlpatterns = [
    path('books/', BooksListView.as_view()),
    path('books/<int:pk>/', BoookViewDetail.as_view()),
    path('db/', PostBooks.as_view()),
]