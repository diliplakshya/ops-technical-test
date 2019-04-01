"""
This module is the model class responsible for creating Database tables for Home
and Meta Data View.
"""


from django.db import models


class Home(models.Model):
    """
    Creates database table for Home View.
    @display_text: To display text on home page.
    """
    display_text = models.CharField(max_length=200)

    def __str__(self):
        """
        String represantation for Home object.
        """
        return f'{self.display_text}'

class MetaData(models.Model):
    """
    Creates database table for Meta Data View.
    @version: Application version, e.g. 1.0.
    @description: Application description.
    @last_commit_sha: Last github commit sha.
    @commit_message: Last github commit message.
    """
    version = models.CharField(max_length=10)
    description = models.TextField()
    last_commit_sha = models.CharField(max_length=50, blank=True)
    commit_message = models.CharField(max_length=200, default='Code Commit')

    def __str__(self):
        """
        String represantation for Meta Data object.
        """
        return f'{self.version}, {self.description}'
