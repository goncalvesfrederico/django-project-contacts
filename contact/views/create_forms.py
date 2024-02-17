from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm

def create(request):
    if request.method == "POST":
        context = {
            "form": ContactForm(request.POST)
        }

        return render(
            request,
            "contact/create.html",
            context,
        )

    context = {
        "form": ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )