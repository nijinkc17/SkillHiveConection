from django.contrib import admin
from .models import Service,OurServices,Booking

# Register your models here.

admin.site.register(OurServices)
admin.site.register(Service)
admin.site.register(Booking)


