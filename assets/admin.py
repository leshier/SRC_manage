from django.contrib import admin
from assets import models
# Register your models here.
admin.site.register(models.SRC_platform)
admin.site.register(models.Company)
admin.site.register(models.Company_domain)
admin.site.register(models.Company_ips)
admin.site.register(models.Target_sudomain)
admin.site.register(models.Target_ip)
admin.site.register(models.Bug_info)

