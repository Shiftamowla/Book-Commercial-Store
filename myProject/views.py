from django.shortcuts import render,get_object_or_404,redirect
from myApp.models import *

def book_collection(request):
    books = Book.objects.all()
    return render(request, 'book_collection.html', {'books': books})
def book_view(req, id):
    data=Book.objects.filter(id=id)
    text={
        'book':data
    }
    return render(req,'book_view.html',text)

def deletepage(req, id):
    data=Book.objects.filter(id=id)
    data.delete()    
    return redirect("book_collection")

def add_book(req):
    if req.method=='POST':
        title=req.POST.get('title')
        title_link=req.POST.get('title_link')
        image=req.FILES.get('image')

        books=Book(
            title=title,
            title_link=title_link,
            Image=image,
        )
        books.save()
        return redirect('book_collection')
    return render(req,'add_book.html')

