from django.shortcuts import render
from django.http import HttpResponse

def technicaltest(request):
    return HttpResponse("HI. Welcome To MYOB Platform Enablement Technical Test.")
