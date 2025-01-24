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


def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        title_link = request.POST.get('title_link')
        image = request.FILES.get('image')
        author_id = request.POST.get('author')

        author = Author.objects.get(id=author_id)
        
        new_book = Book(
            title=title,
            title_link=title_link,
            Image=image,
            author=author
        )
        new_book.save()

        return redirect('book_collection') 


    authors = Author.objects.all()
    return render(request, 'add_book.html', {'authors': authors})

def edit_book(req, id):

    book = get_object_or_404(Book, id=id)
    authors = Author.objects.all() 
    return render(req, 'edit_book.html', {'book': book, 'authors': authors})

def update(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        book = get_object_or_404(Book, id=id)

        book.title = req.POST.get('title')
        book.title_link = req.POST.get('title_link')
        book.author_id = req.POST.get('author')

        if 'image' in req.FILES:
            book.Image = req.FILES['image'] 
        book.save()

        return redirect('book_collection')
    else:
        return redirect('edit_book', id=id)

