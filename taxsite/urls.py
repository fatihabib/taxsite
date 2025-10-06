from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from siteapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),              # homepage
    path('events/', include('siteapp.urls')),   # events routes
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),         # Django admin
    path('', include('siteapp.urls')),       # siteapp handles homepage, events, contact
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
