from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fnreg(request):
    return HttpResponse("hello this is my registration page")
def fnsample(request):
    return render(request,'sample.html')