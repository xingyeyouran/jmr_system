from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import *
from django.urls import reverse
from django.template import loader
from django.views import generic


# Create your views here.
def index(request):
    return HttpResponse("hello world")
