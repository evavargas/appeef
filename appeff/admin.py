from django.contrib import admin
from .models import Viaje, Auto, Conductor, Favorito

# Register your models here.
class ConductorAdmin(admin.ModelAdmin):
    list_display = ["id", "disponibilidad", "puntuacion"]


class AutoAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "modelo"]


class ViajeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "viajero",
        "conductor",
        "distrito",
        "destino",
        "precio",
        "puntuacion",
        "status",
    ]

    def get_status(self, obj):
        if obj.status == 0:
            return "Activo"
        return "Inactivo"

    get_status.short_description = "status"


class FavoritoAdmin(admin.ModelAdmin):
    list_display = ["id", "user", " distrito", "destino"]


admin.site.register(Auto, AutoAdmin)
admin.site.register(Viaje, ViajeAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Favorito, FavoritoAdmin)
