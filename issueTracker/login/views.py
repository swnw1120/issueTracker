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
    session_key = request.COOKIES.get("session_key")
    if session_key is None:
        form = LoginForm()
        return render(request, 'loginpage.html', { 'loginForm': form })
    return redirect('tracker:homepage')

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
        new_Session.save()
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
        new_Session.save()
        response = redirect('tracker:homepage')
        response.set_cookie('session_key', new_Session_Key)
        return response
    args['form'] = form
    return render(request, 'signuppage.html', { 'SignupForm': form })

def logout(request):
    session_Key = request.COOKIES.get("session_key")
    session_Record = Session.objects.filter(SessionKey=session_Key)
    session_Record.delete()
    response = redirect('loginpage')
    response.delete_cookie('session_key')
    return response