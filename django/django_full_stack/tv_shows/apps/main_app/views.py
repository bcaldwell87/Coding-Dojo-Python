from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Show

def index(request):
    context = {
    'all_shows': Show.objects.all()
}
    return render(request, "main_app/index.html", context)

def newshow(request):

    return render(request, "main_app/newshow.html")

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, error in errors.items():
            messages.error(request, error)
        return redirect('/shows/new')
    else:
        print(request.POST)
        show = Show.objects.create(
            title=request.POST["title"],
            network=request.POST["network"],
            release_date=request.POST["release_date"],
            description=request.POST["description"],
        )
        messages.success(request, "Successfully added a show")
    return redirect(f"/shows/{show.id}")

def viewshow(request, id):
    show_obj = Show.objects.get(id=id)
    context = {
        'show': show_obj
    }
    return render(request, "main_app/viewshow.html", context)

def destroy(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect("/shows")

def edit(request, id):
    show_obj = Show.objects.get(id=id)
    context = {
        'show': show_obj
    }
    return render(request, "main_app/editshow.html", context)

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        print(request.POST)
        the_show = Show.objects.get(id=id)
        the_show.title=request.POST["title"]
        the_show.network=request.POST["network"]
        the_show.release_date=request.POST["release_date"]
        the_show.description=request.POST["description"]
        the_show.save()
        id = the_show.id
        return redirect(f"/shows/{id}")