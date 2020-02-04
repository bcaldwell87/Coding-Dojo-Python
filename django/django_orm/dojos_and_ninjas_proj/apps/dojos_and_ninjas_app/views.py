from django.shortcuts import render

def index(request):
    return render(request, "dojos_and_ninjas_app/index.html")

def new(request):
    return render(request, "dojos_and_ninjas_app/new.html")