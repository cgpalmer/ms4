from django.db import models



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    story = models.TextField()
    sku = models.CharField(max_length=254, null=True, blank=True)
    url = models.URLField(blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    date_taken = models.CharField(max_length=254, null=True, blank=True)    

    def get_title(self):
        return self.title

    def get_story(self):
        return self.story

    def get_url(self):
        return self.url
    
    

        
    