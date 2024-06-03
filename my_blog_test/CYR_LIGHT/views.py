from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("CYR_LIGHT")

def about_it(request):
    return HttpResponse("This would be the about page")