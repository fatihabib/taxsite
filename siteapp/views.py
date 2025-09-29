# siteapp/views.py
from django.shortcuts import render
from .models import Division, Department, Event

def index(request):
    divisions = Division.objects.all()
    events = Event.objects.all()
    context = {
        'divisions': divisions,
        'events': events
    }
    return render(request, 'siteapp/index.html', context)
from django.shortcuts import render, get_object_or_404
from .models import Division, Department, Event

def index(request):
    divisions = Division.objects.all()
    events = Event.objects.all()
    context = {
        'divisions': divisions,
        'events': events
    }
    return render(request, 'siteapp/index.html', context)


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'siteapp/event_detail.html', {'event': event})
