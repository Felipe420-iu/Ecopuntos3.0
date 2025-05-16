from django.contrib import admin
from .models import Proyect

class ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created')
    ordering = ('-created',)
    search_fields = ('title', 'description')
    date_hierarchy = 'created'
    list_filter = ('created', 'updated')

admin.site.register(Proyect, ProyectAdmin)

# Register your models here.
