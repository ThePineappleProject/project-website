from django.contrib import admin
from crops.models import Plant, Cultivar

class CultivarAdmin(admin.ModelAdmin):
    list_display = ("name", "plant")

admin.site.register(Plant)
admin.site.register(Cultivar, CultivarAdmin)

