from django.db import models
from django.conf import settings


# Create your models here.

class Lm(models.Model):
  name = models.CharField(max_length=200)
  desc = models.DateTimeField('date published')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.FileField(upload_to='uploads/%Y/%m/%d/')
  lm_type = models.IntegerField(choices=settings.lm_types)
  lm_lib = models.IntegerField(choices=settings.lm_libs)
  attrs = models.JSONField()