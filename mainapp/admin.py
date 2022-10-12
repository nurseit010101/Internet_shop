from django.contrib import admin
from mainapp.models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','name', 'last_name', 'number',  'address', 'message', 'sent_at')


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order)

admin.site.register(Brand)
admin.site.register(SneakerCard)