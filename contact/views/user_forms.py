from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account have been created.")
            return redirect("contact:login")

    context = {
        "form": form,
    }
    
    return render(
        request,
        "contact/register.html",
        context,
    )


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user=user)
            messages.success(request, "You are successfully logged in!")
            return redirect("contact:index")

    context = {
        "form": form
    }
    return render(
        request,
        "contact/login.html",
        context,
    )

@login_required(login_url="contact:login")
def logout_view(request):
    auth.logout(request)
    return redirect("contact:login")


@login_required(login_url="contact:login")
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method == "POST":
        form = RegisterUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data has been updated")
            return redirect("contact:user_update")

    context = {
        "form": form
    }
    return render(
        request, 
        "contact/user_update.html",
        context,
    )