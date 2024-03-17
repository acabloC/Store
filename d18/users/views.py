from django.shortcuts import render
from d18.users.forms import UserLoginForm
from d18.users.models import User

from django.contrib import auth


def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)


        if form.is_valid():

            username = request.POST[ "username"]
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)

    else:
        form = UserLoginForm()
        context = {"form" : form}

    return render(request, 'users / login.html', context = context)
