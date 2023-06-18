from django.urls import path
from .views import FastFoodHomeView
urlpatterns = [
    path('', FastFoodHomeView.as_view(), name='index')
]