from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, "app_for_users/index.html", context)

def new(request):
    return render(request, "app_for_users/new.html")