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
    commit_message = str()
    response = requests.get(settings.GITHUB_API_URL)

    meta_data = MetaData()
    meta_data.version = '0.0'
    meta_data.description = 'MYOB Pre Interview technical Test'

    if(response.ok):
        response_data = json.loads(response.content)
        lastcommitsha = response_data['sha']
        commit_message = response_data['commit']['message']

        meta_data.last_commit_sha = response_data['sha']
        meta_data.commit_message = response_data['commit']['message']

    meta_data.save()

    meta_data = MetaData.objects.last()
    return render(request, 'technicaltest/about.html', {"meta_data":meta_data})
