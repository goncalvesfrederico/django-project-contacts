from django.shortcuts import render
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")

    # I'm seeing what my SQL QUERY is doing in backend
    print(contacts.query)

    context = {
        "contacts": contacts
    }

    return render(
        request,
        'contact/index.html',
        context
    )