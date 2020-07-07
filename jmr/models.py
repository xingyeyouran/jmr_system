from django.db import models
from django.utils import timezone
import datetime


class JobHunter(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Resume(models.Model):
    JobHunter = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    age = models.IntegerField(default=20)


# Create your models here.
class Enterprise(models.Model):
    enterprise_name = models.CharField(max_length=40)
    enterprise_address = models.CharField(max_length=80)
    enterprise_info = models.CharField(max_length=200)

    def __str__(self):
        return self.enterprise_name
