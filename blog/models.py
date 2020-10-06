from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    story = models.TextField()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_content(self):
        return self.content
    