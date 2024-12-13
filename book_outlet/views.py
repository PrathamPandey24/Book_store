from django.shortcuts import render
from .models import Book, Country, Author, Address
from django.http import Http404
from django.db.models import Avg

# Create your views here.
def index(request):
    books=Book.objects.all()
    num_book=books.count()
    avg_rating=books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html", {"books":books,
                                            "total_number_of_books":num_book,
                                             "average_rating":avg_rating})




def book_detail(request,slug):
    try:
      book=Book.objects.get(slug=slug)
    except:
       raise Http404()
    return render(request,"book_outlet/book_detail.html"
                 , {
                    "title":book.title,
                    "author":book.author,
                    "rating":book.rating,
                    "is_bestseller":book.is_bestselling,
                    "published_in":[country.name for country in book.published_countries.all()]
                  
                 }
                  
                  )