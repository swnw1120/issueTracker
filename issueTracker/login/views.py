from django.shortcuts import render, redirect
import random
import string

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Session
from .forms import LoginForm, SignUpForm

LOGIN_KEY_LEN = 10

def generateKey(key_Length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(key_Length))

def getLoginPage(request):
    form = LoginForm()
    return render(request, 'loginpage.html', { 'loginForm': form })

def postLoginPage(request):
    args = {}
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data["Username"]
        user_object = User.objects.get(Username=username)
        new_Session = Session()
        new_Session_Key = generateKey(LOGIN_KEY_LEN)
        new_Session.SessionKey = new_Session_Key
        new_Session.UserID = user_object
        response = redirect('tracker:homepage')
        response.set_cookie('session_key', new_Session_Key)
        return response
    args['form'] = form
    return render(request, 'loginpage.html', { 'loginForm': form })

def getSignUpPage(request):
    form = SignUpForm()
    return render(request, 'signuppage.html', { 'SignupForm': form })

def postSignUpPage(request):
    args = {}
    form = SignUpForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data["Username"]
        # Create a new user
        new_user = User()
        new_user.Username = username
        new_user.save()
        # Automatically log into the system
        new_Session = Session()
        new_Session_Key = generateKey(LOGIN_KEY_LEN)
        new_Session.SessionKey = new_Session_Key
        new_Session.UserID = new_user
        response = redirect('tracker:homepage')
        response.set_cookie('session_key', new_Session_Key)
        return response
    args['form'] = form
    return render(request, 'signuppage.html', { 'SignupForm': form })