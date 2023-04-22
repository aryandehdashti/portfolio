from django.contrib import admin
from .models import MyInfo, Project, About, Skill
# Register your models here.

admin.site.register(MyInfo)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Skill)