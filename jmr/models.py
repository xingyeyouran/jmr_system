from django.db import models
from django.utils import timezone
import datetime


class JobHunter(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Resume(models.Model):
    JobHunter = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    birthday = models.DateTimeField("birthday", default=timezone.now)
    gender = models.CharField(verbose_name="gender", choices=(('man', '男'), ('woman', '女')), max_length=6)
    major = models.CharField(max_length=40)
    education = models.CharField(max_length=10)
    endowment = models.CharField(max_length=20)
    tel = models.IntegerField(default=2222)
    race = models.CharField(max_length=4)
    family_location = models.CharField(max_length=100)


# Create your models here.
class Enterprise(models.Model):
    enterprise_name = models.CharField(max_length=40)
    enterprise_address = models.CharField(max_length=80)
    enterprise_info = models.CharField(max_length=200)
    enterprise_username = models.CharField(max_length=20, default="aa")
    enterprise_tel = models.IntegerField(verbose_name="telephone")
    enterprise_mail = models.EmailField(max_length=20)

    def __str__(self):
        return self.enterprise_name
