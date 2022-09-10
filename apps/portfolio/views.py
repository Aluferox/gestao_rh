from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
visitors = 0
def home(request,):
    global visitors
    visitors += 1

    if request.method == 'GET':

        return render(request, 'home/home.html', {'visitors': visitors})