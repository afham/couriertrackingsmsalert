from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Container)
admin.site.register(Customer)
