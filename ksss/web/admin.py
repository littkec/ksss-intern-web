from django.contrib import admin
from ksss.web.models import *

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Damage)
admin.site.register(BoatTypes)
admin.site.register(Motors)
admin.site.register(Boat)
admin.site.register(ReportedDamage)
admin.site.register(News)
admin.site.register(InventoryType)
admin.site.register(Building)
admin.site.register(Inventory)
admin.site.register(Camp, ArticleAdmin)
