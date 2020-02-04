from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['activities']= []
    return render(request, 'ng_app/index.html')

def process_money(request):
    print(request.POST['action'])

    if request.POST['action'] == "farm":
        earnings = random.randrange(10, 20)
        request.session['gold'] += earnings
        request.session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the farm! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.POST['action'] == "cave":
        earnings = random.randrange(5, 10)
        request.session['gold'] += earnings
        request.session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the cave! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.POST['action'] == "house":
        earnings = random.randrange(2, 5)
        request.session['gold'] += earnings
        request.session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the house! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.POST['action'] == "casino":
        earnings = random.randrange(-50, 50)
        request.session['gold'] += earnings
        if earnings > 0:
            request.session['activities'].append(
                'Entered a casino and Won ' + str(earnings) + ' gold! Holy Cow! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        else:
            request.session['activities'].append(
                'Entered a casino and Lost ' + str(earnings) + ' gold. Ouch! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())  
            )
    return redirect('/')