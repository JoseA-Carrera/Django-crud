from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    return render(request, 'tasks/home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'tasks/signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('user created successfully')

            except:
                return render(request, 'tasks/signup.html', {
                    'form': UserCreationForm,
                    'error': 'user already exist'
                })

        return render(request, 'tasks/signup.html', {
            'form': UserCreationForm,
            'error': 'password do not match'
        })
