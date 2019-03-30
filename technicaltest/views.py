from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from technicaltest.models import Home, MetaData
import requests


def view_home(request):
    home = Home.objects.last()
    return render(request, 'technicaltest/home.html', {"home":home})

def view_meta_data(request):
    # delete existing records from DB
    MetaData.objects.all().delete()

    meta_data = MetaData()
    meta_data.version = '0.0'
    meta_data.description = 'MYOB Pre Interview technical Test'

    # read last commit from github
    response = requests.get(settings.GITHUB_API_URL)

    if(response.ok):
        meta_data.last_commit_sha = response.json()['sha']
        meta_data.commit_message = response.json()['commit']['message']

    meta_data.save()

    return render(request, 'technicaltest/about.html', {"meta_data":MetaData.objects.last()})
