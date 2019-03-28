from django.shortcuts import render
from django.http import HttpResponse

def technicaltest(request):
    return render(request, 'technicaltest/home.html')
