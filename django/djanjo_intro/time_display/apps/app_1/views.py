from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%B %d, %Y %I:%M %p", gmtime())
    }
    return render(request,'app_1/index.html', context)