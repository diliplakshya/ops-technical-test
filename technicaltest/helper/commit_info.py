import requests


class CommitInfo:
    def __init__(self):
        self.__response_ok = False
        self.__last_commit_sha = None
        self.__commit_message = None

    @property
    def response_ok(self):
        return self.__response_ok

    @response_ok.setter
    def response_ok(self, response_ok):
        self.__response_ok = response_ok

    @property
    def last_commit_sha(self):
        return self.__last_commit_sha

    @last_commit_sha.setter
    def last_commit_sha(self, last_commit_sha):
        self.__last_commit_sha = last_commit_sha

    @property
    def commit_message(self):
        return self.__commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        self.__commit_message = commit_message

    def fetch_commit_info(self, url, token):
        # read last commit from github
        response = None
        try:
            response = requests.get(url, headers={'Authorization': 'TOK:{}'.format(token)})
        except requests.exceptions.MissingSchema as error:
            raise(ValueError(str(error)))

        if(response.ok):
            self.response_ok = True
            self.last_commit_sha = response.json()['sha']
            self.commit_message = response.json()['commit']['message']
