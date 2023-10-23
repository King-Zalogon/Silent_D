from django.db import models

# Create your models here.

class RulesSystem(models.Model):
    system_name = models.CharField(max_length=10, verbose_name="System", default='TBD', null=True)


class Chronicle(models.Model):
    title = models.CharField(max_length=30, verbose_name="Chronicle's title")
    description = models.CharField(verbose_name='Synopsys', null=True)
    gm = models.CharField(max_length=15, verbose_name='Storyteller')
    start = models.DateField(verbose_name='Date of first session', null=True)
    rules_system = models.ForeignKey(RulesSystem, on_delete=models.CASCADE, null=True)
    ended = models.BooleanField(verbose_name="Finished?", default=False)


class Character(models.Model):
    name = models.CharField(max_length=15, verbose_name="Name")
    concept = models.CharField(max_length=30, verbose_name="Concept", default='TBD')
    rules_system = models.ForeignKey(RulesSystem, on_delete=models.CASCADE, null=True)
    growth = models.IntegerField(default=0, verbose_name="Current level or Exp")
    age = models.IntegerField(verbose_name="Age", default=0)
    creator = models.CharField(max_length=15, verbose_name="Creator's name", default='Zalo')
    is_player = models.BooleanField(verbose_name="Is a player's character?", default=True)
    alive = models.BooleanField("Is alive?", default=True)
    bio = models.CharField(max_length=300, verbose_name='Biography', null=True)
    portrait = models.URLField(verbose_name="Portraits' URL", null=True)
    chronicle = models.ForeignKey(Chronicle, on_delete=models.CASCADE, null=True)

