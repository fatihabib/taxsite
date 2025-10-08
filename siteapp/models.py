from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='divisions/', blank=True, null=True)  # add this ✅


    def __str__(self):
        return self.name


class Department(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='divisions/', blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.division.name})"

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='events/')
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)  # <-- Add this field

    def __str__(self):
        return self.title

# siteapp/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'email', 'message')  # prevents exact duplicates

    def __str__(self):
        return f"{self.name} - {self.email}"


from django.shortcuts import render
from .models import Event

def events_page(request):
    events = Event.objects.all().order_by('-date')  # latest events first
    return render(request, 'events.html', {'events': events})
