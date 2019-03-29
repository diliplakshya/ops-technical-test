from django.shortcuts import render
from django.http import HttpResponse
from technicaltest.models import Home, MetaData


def view_home(request):
    home = Home.objects.last()
    return render(request, 'technicaltest/home.html', {"home":home})

def view_meta_data(request):
    meta_data = MetaData.objects.last()
    return render(request, 'technicaltest/about.html', {"meta_data":meta_data})
