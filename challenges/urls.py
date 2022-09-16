from django.urls import path
from . import views

urlpatterns = [
    path("<month>", views.month_challenges)
]

