from django.shortcuts import render
from django.http import HttpResponse
from technicaltest.models import Home, MetaData
from django.conf import settings
from technicaltest.helper.commit_info import CommitInfo

# Home
class ViewHome:
    @classmethod
    def view_home(cls, request):
        return render(request, 'technicaltest/home.html', {"home":Home.objects.last()})

# Home Ends

# MetaData
class ViewMetaData:
    @classmethod
    def view_meta_data(cls, request):
        # delete existing records from DB
        MetaData.objects.all().delete()

        meta_data = MetaData()
        meta_data.version = '0.0'
        meta_data.description = 'MYOB Pre Interview technical Test'

        # read last commit from github
        commit_info = CommitInfo()

        try:
            commit_info.fetch_commit_info(settings.GITHUB_API_URL, settings.GITHUB_AUTH_TOKEN)

            if(commit_info.response_ok):
                meta_data.last_commit_sha = commit_info.last_commit_sha
                meta_data.commit_message = commit_info.commit_message

        except ValueError as error:
            meta_data.last_commit_sha = "abcd1234"
            meta_data.commit_message = "Default Commit Message"

        meta_data.save()

        return render(request, 'technicaltest/about.html', {"meta_data":MetaData.objects.last()})
