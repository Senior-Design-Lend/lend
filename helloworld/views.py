from django.template import loader
from django.shortcuts import render

# Create your views here.

def helloWorld(request):
    return render(request, 'helloworld/index.html')
