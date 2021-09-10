from django.contrib import admin
from .models import User, Busdetails, UserBusmapping,Conductor,Driver,Payment


# Register your models here.
admin.site.register(User)
admin.site.register(Busdetails)
admin.site.register(UserBusmapping)
admin.site.register(Conductor)
admin.site.register(Driver)
admin.site.register(Payment)