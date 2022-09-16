from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def month_challenges(request, month):
    text = None 
    if month == "january":
        text = "Read  at least 10 pages of a book for day"
    elif month == "february":
        text = "wake up at 5:30 every day except the weekends"
    elif month == "march":
        text = "drink more than 2 liters of water a day"
    else:
        return HttpResponseNotFound("Invalid month")
    return HttpResponse(text)