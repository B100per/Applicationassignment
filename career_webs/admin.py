from django.contrib import admin

# Register your models here.
from .models import Software, Gaming, Skill
admin.site.register(Software)
admin.site.register(Gaming)
admin.site.register(Skill)