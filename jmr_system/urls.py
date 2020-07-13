"""jmr_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from jmr import views

# urlpatterns = [
#     path('jmr/', include('jmr.urls')),
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='index'),
    path('job/list', views.jobList, name='jobList'),
    path('job/<int:id>', views.jobDetail, name='jobDetail'),
    path('employee/<int:id>', views.employeeIndex, name='employeeIndex'),
    path('employee/<int:id>/edit/employee_update', views.employeeUpdate, name='employeeUpdate'),
    path('employee/<int:id>/edit/employee_update_handler', views.employeeUpdateHandler, name='employeeUpdateHandler'),
    path('employee/<int:id>/edit/resume_update', views.resumeUpdate, name='resumeUpdate'),
    path('employee/<int:id>/edit/resume_update_handler', views.resumeUpdateHandler, name='resumeUpdateHandler'),
    path('enterprise/list', views.enterpriseList, name='enterpriseList'),
    path('enterprise/<int:id>', views.enterpriseIndex, name='enterpriseIndex'),
    path('enterprise/<int:id>/Detail', views.enterpriseDetail, name='enterpriseDetail'),
    path('enterprise/<int:id>/Jobs', views.enterpriseJobs, name='enterpriseJobs'),
    path('enterprise/<int:id>/edit/enterprise_update', views.enterpriseUpdate, name='enterpriseUpdate'),
    path('enterprise/<int:id>/edit/enterprise_update_handler', views.enterpriseUpdateHandler,
         name='enterpriseUpdateHandler'),
    path('enterprise/<int:id>/edit/job_add', views.enterpriseAddJob, name='enterpriseAddJob'),
    path('enterprise/<int:id>/edit/job_add_handler', views.enterpriseAddJobHandler, name='enterpriseAddJobHandler'),
    path('enterprise/<int:id>/edit/<int:jid>/job_update', views.enterpriseUpdateJob, name='enterpriseUpdateJob'),
    path('enterprise/<int:id>/edit/<int:jid>/job_update_handler', views.enterpriseUpdateJobHandler,
         name='enterpriseUpdateJobHandler'),
    path('enterprise/<int:id>/edit/<int:jid>/job_delete', views.enterpriseDeleteJob, name='enterpriseDeleteJob'),
]
