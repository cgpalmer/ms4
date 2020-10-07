from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    story = models.TextField()

    def get_title(self):
        return self.title

    def get_story(self):
        return self.story
    