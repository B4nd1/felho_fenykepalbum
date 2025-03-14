from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello, world.")

from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html')