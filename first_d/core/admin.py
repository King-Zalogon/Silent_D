from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from core.models import Creator, RulesSystem, Character, Chronicle, GameMaster, Player


class ChronicleAdmin(admin.ModelAdmin):
    list_display = ('title', 'rules_system')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'gm':
            kwargs['queryset'] = Creator.objects.filter(is_gm_is=False). order_by('name')
        
        return super().formfield_for_manytomany(db_field, request, **kwargs)

# Register your models here.
admin.site.register(Creator)
admin.site.register(RulesSystem)
admin.site.register(Character)
admin.site.register(Chronicle, ChronicleAdmin)
admin.site.register(GameMaster)
admin.site.register(Player)
