from django.db import models
from django.utils import timezone
import datetime


class JobHunter(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Resume(models.Model):
    JobHunter = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    age = models.IntegerField()
    birthday = models.DateTimeField("birthday", default=timezone.now)
    major = models.CharField(max_length=40, default='aa')
    education = models.CharField(max_length=10, default='aa')
    endowment = models.CharField(max_length=20, default='aa')
    tel = models.IntegerField(default=2222)
    race = models.CharField(max_length=4, default='aa')
    family_location = models.CharField(max_length=100, default='aa')


# Create your models here.
class Enterprise(models.Model):
    enterprise_name = models.CharField(max_length=40)
    enterprise_address = models.CharField(max_length=80)
    enterprise_info = models.CharField(max_length=200)
    enterprise_username = models.CharField(max_length=20, default="aa")

    def __str__(self):
        return self.enterprise_name
