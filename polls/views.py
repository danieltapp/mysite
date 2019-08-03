from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('yayyyy i did it')

# Create your views here.
