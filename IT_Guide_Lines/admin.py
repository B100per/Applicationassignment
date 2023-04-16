from django.contrib import admin
from .models import SoftwareEngineer,DataEngineer,SecurityEngineer,GameEngineer
# Register your models here.
admin.site.register(SoftwareEngineer)
admin.site.register(DataEngineer)
admin.site.register(SecurityEngineer)
admin.site.register(GameEngineer)