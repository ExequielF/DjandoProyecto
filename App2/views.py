from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    return HttpResponse("<h1 style='color:red'>Hola Mundo 2</h1>")