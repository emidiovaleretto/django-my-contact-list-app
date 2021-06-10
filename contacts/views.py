from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib import messages
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

    if not contacts.to_show:
        raise Http404()

    return render(request, 'contacts/details.html', {
        'contacts': contacts
    })

def search(request):
    term = request.GET.get('term')

    if term is None or not term:
        messages.add_message(
            request,
            messages.ERROR,
            'This field must be filled.'
        )
        return redirect('index')

    contacts = Contact.objects.all().filter(
        name__icontains = term,
    )
    paginator = Paginator(contacts, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/search.html', {
        'contacts': contacts
    })
