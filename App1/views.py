from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def vista1(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")

def vistaDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)

