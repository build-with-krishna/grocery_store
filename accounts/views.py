from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            if user.role == "vendor":
                return redirect('/dashboard/')

            return redirect('/')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_view(request):

    if request.user.is_authenticated:

        if request.user.is_superuser:
            return redirect('/admin/')

        elif request.user.role == "vendor":
            return redirect('/dashboard/')

        else:
            return redirect('/')

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')

            elif user.role == "vendor":
                return redirect('/dashboard/')

            else:
                return redirect('/')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def logout_view(request):

    logout(request)

    return redirect('/accounts/login/')