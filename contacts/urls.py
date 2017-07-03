from django.conf.urls import url
from contacts.views import *

urlpatterns = [
    url(r'^$', ContactListView.as_view(), name='contact-list'),
    url(r'^(?P<pk>\d+)$', ContactDetailView.as_view(), name='contact-detail'),
    url(r'^add', ContactCreateView.as_view(), name='contact-create'),
    url(r'^(?P<pk>\d+)/edit', ContactUpdateView.as_view(), name='contact-edit'),
    url(r'^(?P<pk>\d+)/delete', ContactDeleteView.as_view(), name='contact-delete'),
]
