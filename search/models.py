from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CoursesModel(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)
    address = models.CharField(max_length=255)
