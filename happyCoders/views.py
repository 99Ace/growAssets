from django.shortcuts import render, HttpResponse

# Create your views here.


def happyCoders(request):
    return HttpResponse("Happy Coders Home")
