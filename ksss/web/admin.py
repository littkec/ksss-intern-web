from django.contrib import admin
from ksss.web.models import *



class BoatAdmin(admin.ModelAdmin):
    list_display = ['name', 'boat_type', 'home_port']
admin.site.register(Boat, BoatAdmin)

class UploadAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Upload, UploadAdmin)

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Camp, ArticleAdmin)



admin.site.register(Position)
admin.site.register(Damage)
admin.site.register(BoatTypes)
admin.site.register(Motors)
admin.site.register(ReportedDamage)
admin.site.register(News)
admin.site.register(InventoryType)
admin.site.register(Building)
admin.site.register(Inventory)
