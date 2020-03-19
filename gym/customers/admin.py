from django.contrib import admin

from .models import Subscribes, Activities, Customer

admin.site.register(Subscribes)
admin.site.register(Customer)
admin.site.register(Activities)
