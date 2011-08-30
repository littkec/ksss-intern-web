from django.contrib import admin
from ksss.web.models import Damage, Boat, ReportedDamage


admin.site.register(Boat)
admin.site.register(Damage)
admin.site.register(ReportedDamage)

