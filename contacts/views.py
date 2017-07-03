from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contact
from django.urls import reverse_lazy


class ContactListView(ListView):
    model = Contact
    paginate_by = 5


class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'image']


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['name', 'email', 'image']


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact-list')
