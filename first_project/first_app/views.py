from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def training(request, domain_id):
    return HttpResponse('You are in this:', domain_id)
