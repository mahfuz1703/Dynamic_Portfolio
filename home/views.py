from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime

# Create your views here.
def myNameIsKhan(request):
    about = About.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()


    current_year = datetime.datetime.now().year
    context = {
        'about': about,
        'education': education,
        'experience': experience,

        
        'currentYear':current_year,
    }
    return render(request, "home/index.html", context)