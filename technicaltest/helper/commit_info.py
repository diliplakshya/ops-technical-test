"""
This module talks to github REST API and fetches the last commit sha and message.
This module is called by MetaData View class.
"""

import requests


class CommitInfo:
    """
    This class is responsible for getting last commit info from github.
    """
    def __init__(self):
        """
        CommitInfo Constructor.
        """
        self.__response_ok = False
        self.__last_commit_sha = None
        self.__commit_message = None

    @property
    def response_ok(self):
        """
        Getter method for self.__response_ok
        """
        return self.__response_ok

    @response_ok.setter
    def response_ok(self, response_ok):
        """
        Setter method for self.__response_ok
        """
        self.__response_ok = response_ok

    @property
    def last_commit_sha(self):
        """
        Getter method for self.__last_commit_sha
        """
        return self.__last_commit_sha

    @last_commit_sha.setter
    def last_commit_sha(self, last_commit_sha):
        """
        Setter method for self.__last_commit_sha
        """
        self.__last_commit_sha = last_commit_sha

    @property
    def commit_message(self):
        """
        Getter method for self.__commit_message
        """
        return self.__commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """
        Setter method for self.__commit_message
        """
        self.__commit_message = commit_message

    def fetch_commit_info(self, url):
        """
        Read last commit from github.
        Raises ValueError exception if string is not a url type.
        If Response is OK then it saves commit sha and message into private variables,
        which can be accessed using @property of code and message
        """
        response = None
        try:
            response = requests.get(url)
        except requests.exceptions.MissingSchema as error:
            raise(ValueError(str(error)))

        if(response.ok):
            self.response_ok = True
            self.last_commit_sha = response.json()['sha']
            self.commit_message = response.json()['commit']['message']
