from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=15, verbose_name='Name')
    concept = models.CharField(max_length=30, verbose_name='Concept', default='TBD')
    rules_system = models.CharField(max_length=10, verbose_name='System', default='TBD')
    age = models.IntegerField(verbose_name='Age', default=0)
