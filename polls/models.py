from django.db import models

# Create your models here.
class Vote(models.Model):
    name = models.CharField(max_length=100, default='')
    is_vote = models.BooleanField(default=False)