from django.shortcuts import render
from myApp.models import *

def book_collection(request):
    books = Book.objects.all()
    return render(request, 'book_collection.html', {'books': books})
