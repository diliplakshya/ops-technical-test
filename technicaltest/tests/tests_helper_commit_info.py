"""
This module contains the unit tests for commit_info.py module.
"""


from django.test import TestCase
from django.conf import settings
from technicaltest.helper.commit_info import CommitInfo


class CommitInfoTests(TestCase):
    """
    Unit tests for commit_info.py module.
    """
    @classmethod
    def setUpTestData(cls):
        cls.commit_info = CommitInfo()

    def test_response_ok_setter_getter(self):
        CommitInfoTests.commit_info.response_ok = True                      # Property setter method is called
        self.assertEquals(CommitInfoTests.commit_info.response_ok, True)    # Property getter method is called

    def test_last_commit_sha_setter_getter(self):
        CommitInfoTests.commit_info.last_commit_sha = "a1b2c3d4"                      # Property setter method is called
        self.assertEquals(CommitInfoTests.commit_info.last_commit_sha, "a1b2c3d4")    # Property getter method is called

    def test_commit_message_setter_getter(self):
        CommitInfoTests.commit_info.commit_message = "new code commit"                      # Property setter method is called
        self.assertEquals(CommitInfoTests.commit_info.commit_message, "new code commit")    # Property getter method is called

    def test_fetch_commit_info_raises_exception(self):
        url = "inavlid_url"

        with self.assertRaises(ValueError): CommitInfoTests.commit_info.fetch_commit_info(url)()

    def test_fetch_commit_info_response_ok_on_valid_url_and_token(self):
        CommitInfoTests.commit_info.fetch_commit_info(settings.GITHUB_API_URL)
        self.assertTrue(CommitInfoTests.commit_info.response_ok)
