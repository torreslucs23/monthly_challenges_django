from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def january(response):
    return HttpResponse("eat no meat for the enire month")


def february(response):
    return HttpResponse("walk for at least 20 minutes every day!")

