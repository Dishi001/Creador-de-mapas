from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.") #cuando yo visite el home, me va a devolver este mensaje
    return render (request, 'index.html')