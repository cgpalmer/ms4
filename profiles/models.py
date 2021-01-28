from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=False, blank=True, default="*")
    default_country = CountryField(blank_label='Country *', null=False, blank=True, default="UK")
    default_postcode = models.CharField(max_length=20, null=False, blank=True, default="*")
    default_town_or_city = models.CharField(max_length=40, null=False, blank=True, default="*")
    default_street_address1 = models.CharField(max_length=80, null=False, blank=True, default="*")
    default_street_address2 = models.CharField(max_length=80, null=False, blank=True, default="*")
    default_county = models.CharField(max_length=80, null=False, blank=True, default="*")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class ContentReadyToDownload(models.Model):
    user = models.CharField(max_length=254, null=False, blank=True, default="Anonymous")
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=False, blank=True, default="Purchase")
    number_of_times_downloaded = models.BooleanField(default=False)
    product = models.ForeignKey('products.Product', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Image_upload(models.Model):
    user = models.CharField(max_length=254, null=False, blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    user_upload_image_file_path = models.CharField(max_length=200, default="not found")
    # You don't need this download
    downloaded = models.BooleanField(default=False)
    sku = models.CharField(max_length=254, default=str(uuid.uuid4()), null=False, blank=False)

    def __str__(self):
        return self.title
