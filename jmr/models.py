from django.db import models
from django.utils import timezone as datetime


class Enterprise(models.Model):
    enterprise_name = models.CharField(max_length=40)
    enterprise_account = models.CharField(max_length=20)
    enterprise_password = models.CharField(max_length=40)
    enterprise_address = models.CharField(max_length=80, default='address')
    enterprise_tel = models.IntegerField(verbose_name='telephone', default=12345)
    enterprise_mail = models.EmailField(max_length=20, default='mail')
    enterprise_info = models.CharField(max_length=200, default='info')

    def __str__(self):
        return self.enterprise_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=40)
    employee_account = models.CharField(max_length=40)
    employee_password = models.CharField(max_length=40)

    def __str__(self):
        return self.employee_name


class Resume(models.Model):
    resume_birthday = models.DateTimeField("birthday", default=datetime.now)
    resume_gender = models.CharField(verbose_name='gender', choices=(('man', '男'), ('woman', '女')), max_length=6,
                                     default='man')
    resume_race = models.CharField(max_length=4, default='汉')
    resume_school = models.CharField(max_length=40, default='school')
    resume_degree = models.CharField(max_length=40, default='degree')
    resume_major = models.CharField(max_length=40, default='major')
    resume_tel = models.IntegerField(default=12345)
    resume_mail = models.EmailField(max_length=20, default='mail')
    resume_employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    resume_info = models.CharField(max_length=200, default='info')
    resume_address = models.CharField(max_length=80, default='address')

    def __str__(self):
        return self.resume_employee.employee_name


class Job(models.Model):
    job_name = models.CharField(max_length=40)
    job_school = models.CharField(max_length=40, default='school')
    job_degree = models.CharField(max_length=40, default='degree')
    job_major = models.CharField(max_length=40, default='major')
    job_salary = models.IntegerField(default=10000)
    job_count = models.IntegerField(default=1)
    job_info = models.CharField(max_length=200, default='info')
    job_enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    job_resume = models.ManyToManyField(Resume, null=True)

    def __str__(self):
        return self.job_name
