from django.http import HttpResponse
from django.shortcuts import render

def new_route(request):
    context = {}
    return render(request, 'UWHackathonProject/homepage.html', context)
