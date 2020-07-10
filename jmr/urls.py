from . import views
from django.urls import path

app_name = "jmr"
urlpatterns = [
    path('', views.index, name='hello'),
    path('login/', views.login, name='login'),
    path('resume/',views.resume,name='resume'),
    path('enterprise/',views.enterprise,name='enterprise'),
]
