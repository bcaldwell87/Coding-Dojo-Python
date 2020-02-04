from django.shortcuts import render, HttpResponse, redirect
from .models import User, Job
from django.contrib import messages

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
        return redirect('/dashboard')

def login(request):
    result = User.objects.check_login(request.POST)
    if result[0] == False:
        messages.error(request, result[1])
        return redirect ('/')
    else:
        request.session['user_id'] = result[1].id
        request.session['user_first_name'] = result[1].first_name
        return redirect('/dashboard')

def dashboard(request):
    jobs_list = Job.objects.all()
    context = {
        "all_jobs": jobs_list,
        "current_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "beltapp/dashboard.html", context)

def newjob(request):
    return render(request, "beltapp/newjob.html")

def createjob(request):
    print(request.POST)
    job_obj = Job.objects.validate(request.POST)
    if len(job_obj) > 0:
        for err in job_obj:
            messages.error(request, err)
        return redirect ('/jobs/new')
    else:
        current_user = User.objects.get(id=request.session['user_id'])
        job_obj = Job.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            location=request.POST['location'],
            uploader=current_user,
        )
        job_obj.seeker.add(current_user)
        return redirect('/dashboard')

def show_job(request, id):
    job_obj = Job.objects.get(id=id)
    context = {
        'job': job_obj
    }
    return render(request, "beltapp/showjob.html", context)

def addjob(request, id):
    job_obj = Job.objects.get(id=id)
    current_user = User.objects.get(id=request.session['user_id'])
    job_obj.seeker.add(current_user)
    return redirect('/dashboard')

def edit(request, id):
    job_obj = Job.objects.get(id=id)
    context = {
        'job': job_obj
    }
    return render(request, "beltapp/edit.html", context)

def update(request, id):
    job_obj = Job.objects.validate(request.POST)
    if len(job_obj) > 0:
        for err in job_obj:
            messages.error(request, err)
        return redirect(f'/jobs/{id}/edit')
    else:
        job_obj = Job.objects.get(id=id)
        job_obj.title= request.POST['title']
        job_obj.desc= request.POST['desc']
        job_obj.location= request.POST['location']
        job_obj.save()
        return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')