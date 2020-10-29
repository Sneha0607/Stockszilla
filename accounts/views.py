from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
<<<<<<< HEAD
from .models import Fund,Point
from .forms import SignUpForm, LoginForm


#class signup_view(generic.CreateView):
 #   form_class = SignUpForm
  #  template_name = 'accounts/signup.html'
   # success_url = reverse_lazy('login')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            money = 100000.00
            login(request, user)
            newfund = Fund(funds=money, user=request.user)
            newfund.save()
            newpoint = Point(points=0.0, user=user.request)
            newpoint.save()
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
