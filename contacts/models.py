from django.urls import reverse
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='images', default='images/noimages.jpg')
    last_contacted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
