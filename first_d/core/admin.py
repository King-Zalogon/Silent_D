from django.contrib import admin
from core.models import Creator, RulesSystem, Character, Chronicle

# Register your models here.
admin.site.register(Creator)
admin.site.register(RulesSystem)
admin.site.register(Character)
admin.site.register(Chronicle)