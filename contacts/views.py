from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })

def details(request, contact_id):
    contacts = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/details.html', {
        'contacts': contacts
    })
