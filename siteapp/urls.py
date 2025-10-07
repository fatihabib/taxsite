from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),                       # Homepage
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  # Event detail
    path('contact/', views.contact_view, name='contact'),      # Contact page
]
