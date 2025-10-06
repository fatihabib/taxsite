from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('event/<int:event_id>/', views.event_detail, name='event_detail'),
#     path("contact/", views.contact, name="contact"),  

# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                      # homepage
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path("contact/", views.contact_view, name="contact"),
       # contact form
]
