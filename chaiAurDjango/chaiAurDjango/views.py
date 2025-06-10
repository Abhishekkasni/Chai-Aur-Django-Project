from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world, this is home page of chaiAurDjango website!🏠")
    return render(request,'website/index.html')

def about(request):
     return render(request,'website/about.html')
    # return HttpResponse("Hello world, this is about page of chaiAurDjango website!🤔")

def contact(request):
     return render(request,'website/contact.html')
    # return HttpResponse("Hello world, this is contact page of chaiAurDjango website!✉️")
