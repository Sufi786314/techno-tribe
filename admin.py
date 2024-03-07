from django.contrib import admin
# from app.models import CustomUser
from app.models import Employee,MaterialIn,MaterialOut
# Register your models here.
admin.site.register(Employee)
admin.site.register(MaterialIn)
admin.site.register(MaterialOut)