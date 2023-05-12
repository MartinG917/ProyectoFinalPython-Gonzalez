from django.shortcuts import render
from typing import Any,Dict
from django.http import HttpResponse



def inicio(request):
    return render(request,'App1/inicio.html')
def kobe(request):
    return render(request,'App1/kobe.html')