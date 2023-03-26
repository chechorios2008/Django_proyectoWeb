from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'created')

# (Servicio) => El nombre de la clase que estoy registrando
admin.site.register(Servicio, ServicioAdmin)