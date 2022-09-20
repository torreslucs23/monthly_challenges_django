from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), #/challenges/
    path("<int:month>", views.month_challenges_by_number),
    path("<str:month>", views.month_challenges, name = "month-challenge" ) #dynamic path
    
]
#here the url patterns help me to create the path to the views. We have prioeity top-down
#in the lecture of the program


