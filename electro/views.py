from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def car1(request):
    return HttpResponse('Byd')

def car2(request):
    return HttpResponse('Tesla')
