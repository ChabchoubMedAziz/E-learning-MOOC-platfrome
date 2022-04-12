from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login ,logout

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'account/signup.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('index')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('index')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('index')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'account/login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'index.html')


def customer(request):
    return render(request,'index.html')


def employee(request):
    return render(request,'index.html')

def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")
    return render(request, "account/logout.html")