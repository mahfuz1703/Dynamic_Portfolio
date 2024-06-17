from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime
import requests

# Create your views here.
def get_cf_user_info(handle):
    url = 'https://codeforces.com/api/user.info'
    params = {'handles': handle}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result'][0]
    return None

def get_cf_user_status(handle):
    url = 'https://codeforces.com/api/user.status'
    params = {'handle': handle}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result']
    return []


def get_cc_user_info(handle):
    url = f'https://codechef-api.vercel.app/{handle}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            return {
                'profile': data['profile'],
                'name': data['name'],
                'currentRating': data['currentRating'],
                'highestRating': data['highestRating'],
                'countryFlag': data['countryFlag'],
                'countryName': data['countryName'],
                'globalRank': data['globalRank'],
                'countryRank': data['countryRank'],
                'stars': data['stars'],
                'heatMap': data['heatMap'],
                'ratingData': data['ratingData']
            }
    return None


def get_lc_user_info(handle):
    url = f'https://alfa-leetcode-api.onrender.com/userProfile/{handle}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'totalSolved': data['totalSolved'],
            'easySolved': data['easySolved'],
            'mediumSolved': data['mediumSolved'],
            'hardSolved': data['hardSolved'],
        }
    return None

def myNameIsKhan(request):
    about = About.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    contest = Contest.objects.all()
    projects = Projects.objects.all()
    recommends = Recommendation.objects.all()
    blogs = Blog.objects.all()

    # fetch codeforces user information
    cf_handle = request.GET.get('handle', 'Tech.Wolf')
    cf_user_info = get_cf_user_info(cf_handle)
    cf_submissions = get_cf_user_status(cf_handle)
    cf_totalSolved = 0
    for submission in cf_submissions:
        if submission['verdict'] == 'OK':
            cf_totalSolved += 1

    # fetch codechef user information
    cc_handle = request.GET.get('handle', 'mahfuzmia1703')
    cc_user_info = get_cc_user_info(cc_handle)

    # fatch leetcode user information
    lc_handle = request.GET.get('handle', 'mahfuzmia1703')
    lc_user_info = get_lc_user_info(lc_handle)


    totalProblemSolved = cf_totalSolved;
    current_year = datetime.datetime.now().year
    context = {
        'about': about,
        'education': education,
        'experience': experience,
        'contest': contest,
        'projects': projects,
        'recommends': recommends,
        'blogs': blogs,

        'user_info': cf_user_info,

        'cc_user_info': cc_user_info,
        'lc_user_info': lc_user_info,
        
        'totalSolved': totalProblemSolved,
        'currentYear':current_year,
    }
    return render(request, "home/index.html", context)