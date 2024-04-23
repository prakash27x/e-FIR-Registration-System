from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "national_id", "email")
    search_fields = ("full_name", "phone", "national_id", "email")
    ordering = ("full_name", )

admin.site.register(Form, FormAdmin)