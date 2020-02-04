from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, "bookauthorapp/index.html", context)

def addbook(request):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
    return redirect(request, "bookauthorapp/index.html")

def book(request, id):
    book_obj = Book.objects.get(id=id)
    context = {
        'book': book_obj
    }
    return render(request, "bookauthorapp/book.html", context)

def authorsbook(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, "bookauthorapp/book.html", context)

def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, "bookauthorapp/authors.html", context)

def author(request, id):
    author_obj = Author.objects.get(id=id)
    context = {
        'author': author_obj
    }
    return render(request, "bookauthorapp/viewauthor.html", context)

def bookauthors(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, "bookauthorapp/viewauthor.html", context)

def addauthor(request):
    if request.method == "POST":
        val_for_first_name = request.POST["first_name"]
        val_for_last_name = request.POST["last_name"]
        val_for_notes = request.POST["notes"]
    return redirect(request, "bookauthorapp/authors.html")