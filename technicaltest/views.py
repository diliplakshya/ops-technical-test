from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from technicaltest.models import Home, MetaData
import requests
import json


def view_home(request):
    home = Home.objects.last()
    return render(request, 'technicaltest/home.html', {"home":home})

def view_meta_data(request):
    # delete existing records from DB
    MetaData.objects.all().delete()

    # read last commit from github
    lastcommitsha = "abcd1234"
    response = requests.get(settings.GITHUB_API_URL)

    if(response.ok):
        response_data = json.loads(response.content)
        lastcommitsha = response_data['sha']

    meta_data = MetaData(version='1.0', description='MYOB Pre Interview technical Test', lastcommitsha=lastcommitsha)
    meta_data.save()

    meta_data = MetaData.objects.last()
    return render(request, 'technicaltest/about.html', {"meta_data":meta_data})
