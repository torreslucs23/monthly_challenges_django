from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



# Create your views here.

#this dict is to do a dynamic path to each month
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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        #capitalize the month's string
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        #we print all the months links
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


#this function test if the month is valid, using the string. Also
#it works with the dict created up here
def month_challenges(request, month):
    text_response = None
    title = month + "'s challenge"
    try:
        text_response = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": text_response,
            "month": month,
            "title": title})
        
    except:
        return HttpResponseNotFound("<h1>Invalid month</h1>")


#this fuunction is to show the right month with a number.
#Also redirect the request
def month_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge" , args = [redirect_month])
    return HttpResponseRedirect(redirect_path)
