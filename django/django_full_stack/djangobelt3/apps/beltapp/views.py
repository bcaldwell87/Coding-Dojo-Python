from django.shortcuts import render, HttpResponse, redirect
from .models import User, Wish
from django.contrib import messages
from datetime import datetime

def index(request):
    return render(request, "beltapp/index.html")

def register(request):
    result = User.objects.validate(request.POST)
    if result[0] == False:
        for err in result[1]:
            messages.error(request, err)
        return redirect ('/')
    else:
        request.session['user_id'] = result[1].id
        request.session['user_first_name'] = result[1].first_name
        return redirect('/wishes')

def login(request):
    result = User.objects.check_login(request.POST)
    if result[0] == False:
        messages.error(request, result[1])
        return redirect ('/')
    else:
        request.session['user_id'] = result[1].id
        request.session['user_first_name'] = result[1].first_name
        return redirect('/wishes')

def dashboard(request):
    user_in_session = User.objects.get(id=request.session['user_id'])
    taken = Wish.objects.filter(giver=user_in_session)
    grantedwish = Wish.objects.exclude(giver=user_in_session)
    context = {
        "taken": taken,
        "grantedwish": grantedwish,
        "current_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "beltapp/dashboard.html", context)

def newwish(request):
    return render(request, "beltapp/newwish.html")

def createwish(request):
    print(request.POST)
    wish_obj = Wish.objects.validate(request.POST)
    if len(wish_obj) > 0:
        for err in wish_obj:
            messages.error(request, err)
        return redirect ('/wish/new')
    else:
        current_user = User.objects.get(id=request.session['user_id'])
        wish_obj = Wish.objects.create(
            item=request.POST['item'],
            desc=request.POST['desc'],
            uploader=current_user,
        )
        wish_obj.giver.add(current_user)
        return redirect('/wishes')

def destroywish(request, id):
    wish_to_delete = Wish.objects.get(id=id)
    wish_to_delete.delete()
    return redirect('/wishes')

def edit(request, id):
    wish_obj = Wish.objects.get(id=id)
    context = {
        'wish': wish_obj
    }
    return render(request, "beltapp/edit.html", context)

def update(request, id):
    wish_obj = Wish.objects.validate(request.POST)
    if len(wish_obj) > 0:
        for err in wish_obj:
            messages.error(request, err)
        return redirect(f'/wishes/edit/{id}')
    else:
        wish_obj = Wish.objects.get(id=id)
        wish_obj.item= request.POST['item']
        wish_obj.desc= request.POST['desc']
        wish_obj.save()
        return redirect('/wishes')

def wishgranted(request, id):
    user = User.objects.get(id=request.session['user_id'])
    wish = Wish.objects.get(id=id)
    user.wish_granted.remove(wish)
    return redirect('/wishes')

def logout(request):
    request.session.clear()
    return redirect('/')