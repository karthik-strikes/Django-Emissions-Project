from django.contrib import admin
from .models import Emissions

@admin.register(Emissions)
class EmissionsAdmin(admin.ModelAdmin):
    list_display = ['date_created', 'accounting_period', 'scope_1', 'scope_2', 'scope_3']
