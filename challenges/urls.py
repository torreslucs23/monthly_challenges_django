from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.month_challenges_by_number),
    path("<str:month>", views.month_challenges)
    
]

