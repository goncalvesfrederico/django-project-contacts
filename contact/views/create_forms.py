from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact

def create(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")

    context = {
        
    }

    return render(
        request,
        'contact/create.html',
        context
    )