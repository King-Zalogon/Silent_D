from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=15, verbose_name="Name")
    concept = models.CharField(max_length=30, verbose_name="Concept", default='TBD')
    rules_system = models.CharField(max_length=10, verbose_name="System", default='TBD', null=True)
    growth = models.IntegerField(default=0, verbose_name="Current level or Exp")
    age = models.IntegerField(verbose_name="Age", default=0)
    creator = models.CharField(max_length=15, verbose_name="Creator's name", default='Zalo')
    is_player = models.BooleanField(verbose_name="Is a player's character?", default=True)
    alive = models.BooleanField("Is alive?", default=True)
    bio = models.CharField(max_length=300, verbose_name='Biography', null=True)
    portrait = models.URLField(verbose_name="Portraits' URL", null=True)
    
