from idlelib.autocomplete import FILES

from django.contrib import messages, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import NewUserForm
from .models import farmer, farm, cli


# Create your views here.
def cos(request):
    return render(request, "color.html")
def demo(request):
    return HttpResponse('welcome')

def tem(request):
    q = farmer.objects.all()
    w = farm.objects.all()
    t = cli.objects.all()
    return render(request, 'index.html', {'name': q, 'aa': w, 'dd': t})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")

            return redirect('dd')
    else:
        form = NewUserForm()
    return render(request, "register.html", {"register_form": form})


def login_request(request, form=None):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("rr")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
def logout_request(request):
    auth.logout(request)
    return redirect("login")

