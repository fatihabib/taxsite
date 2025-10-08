from django.contrib import admin
from .models import Division, Department, Event

class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [DepartmentInline]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'image','division')  # 👈 shows image field in admin

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)
from django.contrib import admin
from .models import Event


