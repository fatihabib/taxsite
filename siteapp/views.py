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
# siteapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        # 1️⃣ Prevent exact duplicates
        if ContactMessage.objects.filter(name=name, email=email, message=message).exists():
            return JsonResponse({
                "status": "error",
                "message": "Duplicate message detected. You have already sent this."
            })

        # 2️⃣ Optional cooldown: prevent sending more than 1 message per minute per email
        one_minute_ago = timezone.now() - timedelta(minutes=1)
        recent = ContactMessage.objects.filter(email=email, created_at__gte=one_minute_ago)
        if recent.exists():
            return JsonResponse({
                "status": "error",
                "message": "Please wait before sending another message."
            })

        # 3️⃣ Save message safely
        try:
            with transaction.atomic():
                ContactMessage.objects.create(name=name, email=email, message=message)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": "An unexpected error occurred. Try again later."
            })

        # 4️⃣ Return success response
        return JsonResponse({"status": "success"})

    # GET request → render contact page
    return render(request, "siteapp/contact.html")
