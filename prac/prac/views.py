from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("You are at django view httprespponse")
    return render(request,'website/index.html')


def contact(request):
    return HttpResponse("You are at django view contact httprespponse")

def about(request):
    return HttpResponse("You are at django view about httprespponse")