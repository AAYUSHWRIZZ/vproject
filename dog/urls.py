
from django.urls import path

from django.shortcuts import HttpResponse

def dog_home(request):
    return HttpResponse("Dog Home")

def tommy(request):
    return HttpResponse("Tommy page")


urlpatterns = [
    path('', dog_home),
    path('tommy', tommy),

]
