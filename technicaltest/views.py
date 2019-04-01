"""
This module takes requests redirected by urls.py module.
This modules reads the database tables and fetches data and
passes it on to template (html files) which are returned back to client.
"""


from django.shortcuts import render
from django.http import HttpResponse
from technicaltest.models import Home, MetaData
from django.conf import settings
from technicaltest.helper.commit_info import CommitInfo

# Home
class ViewHome:
    """
    Recieves requests redirected by urls.py module for Home view.
    """
    @classmethod
    def view_home(cls, request):
        """
        Returns HTTP response to client for Home view.
        """
        Home.objects.all().delete()
        Home.objects.create(display_text="MYOB Web App")
        return render(request, 'technicaltest/home.html', {"home":Home.objects.last()})

# Home Ends

# MetaData
class ViewMetaData:
    """
    Recieves requests redirected by urls.py module for Meta Data view.
    """
    @classmethod
    def view_meta_data(cls, request):
        """
        Returns HTTP response to client for Meta Data view.
        """
        # delete existing records from DB
        MetaData.objects.all().delete()

        meta_data = MetaData()
        meta_data.version = '0.0'
        meta_data.description = 'MYOB Pre Interview technical Test'

        # read last commit from github
        commit_info = CommitInfo()

        try:
            # Reads Git Hub API URL from settings.py module.
            commit_info.fetch_commit_info(settings.GITHUB_API_URL)

            # if REST API request is successful
            if(commit_info.response_ok):
                meta_data.last_commit_sha = commit_info.last_commit_sha
                meta_data.commit_message = commit_info.commit_message

        except ValueError as error:
            # Commit sha and message could not be fetched. Use default values
            meta_data.last_commit_sha = "abcd1234"
            meta_data.commit_message = "Default Commit Message"

        # Save data to database.
        meta_data.save()

        # return response to client by reading last record from database.
        return render(request, 'technicaltest/about.html', {"meta_data":MetaData.objects.last()})
