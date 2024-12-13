from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index),
    path("<slug:slug>",views.book_detail, name="book-detail")
    ]