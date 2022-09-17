from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

monthly_challenges = {
    "january": "Read  at least 10 pages of a book for day",
    "february": "wake up at 5:30 every day except the weekends",
    "march": "drink more than 2 liters of water a day", 
    "april": "go to the gym",
    "may": "study english",
    "june": "use less socia media",
    "july": "start learn data science",
    "august": "start learn italian",
    "september": "eat no meat for the entire month",
    "october": "do not drink soda for the entire month",
    "november": "start learn about deep learning",
    "december": "do a voluntary work"
}


def month_challenges(request, month):
    text = None
    try:
        text = monthly_challenges[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Invalid month")



def month_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)
