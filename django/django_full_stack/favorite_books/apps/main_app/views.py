from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book
from django.contrib import messages

def index(request):
    return render(request, "main_app/index.html")

def register(request):
    result = User.objects.validate(request.POST)
    if result[0] == False:
        for err in result[1]:
            messages.error(request, err)
        return redirect ('/')
    else:
        request.session['user_id'] = result[1].id
        request.session['user_first_name'] = result[1].first_name
        return redirect('/books')

def login(request):
    result = User.objects.check_login(request.POST)
    if result[0] == False:
        messages.error(request, result[1])
        return redirect ('/')
    else:
        request.session['user_id'] = result[1].id
        request.session['user_first_name'] = result[1].first_name
        return redirect('/books')

def books(request):
    books_list = Book.objects.all()
    context = {
        "all_books": books_list,
        "current_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "main_app/books.html", context)

def create_book(request):
    print(request.POST)
    book_obj = Book.objects.validate(request.POST)
    if len(book_obj) > 0:
        for err in book_obj[1]:
            messages.error(request, err)
        return redirect ('/books')
    else:
        current_user = User.objects.get(id=request.session['user_id'])
        book_obj = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            uploader=current_user,
        )
        book_obj.fans.add(current_user)
        return redirect('/books')

def show_book(request, id):
    book_obj = Book.objects.get(id=id)
    context = {
        'book': book_obj
    }
    current_user = User.objects.get(id=request.session['user_id'])
    if current_user ==  book_obj.uploader:
        return render(request, "main_app/editbook.html", context)
    else:
        return render(request, "main_app/show.html", context)

def update(request, book_id):
    book_obj = Book.objects.validate(request.POST)
    if len(book_obj) > 0:
        for err in book_obj[1]:
            messages.error(request, err)
        return redirect ('/books')
    else:
        book_obj = Book.objects.get(id=book_id)
        book_obj.title= request.POST['title']
        book_obj.desc= request.POST['desc']
        book_obj.save()
        return redirect('/books')

def delete_book(request, id):
    book_to_delete = Book.objects.get(id=id)
    book_to_delete.delete()
    return redirect("/books")

def unfavorite(request, id):
    book_to_unfav = Book.favorite_books.get(id=id)
    book_to_unfav.delete()
    return redirect("/books")

def addfavorite(request, book_id):
    book_obj = Book.objects.get(id=book_id)
    current_user = User.objects.get(id=request.session['user_id'])
    book_obj.fans.add(current_user)
    return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')