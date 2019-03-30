from django.db import models

class Home(models.Model):
    display_text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.display_text}'

class MetaData(models.Model):
    version = models.CharField(max_length=10)
    description = models.TextField()
    last_commit_sha = models.CharField(max_length=50, blank=True)
    commit_message = models.CharField(max_length=200, default='Code Commit')

    def __str__(self):
        return f'{self.version}, {self.description}'
