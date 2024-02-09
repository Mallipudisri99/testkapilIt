from django.db import models
from django.contrib.auth.models import User 
from taggit.managers import TaggableManager

from django.conf import settings

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/%Y/%m/%d', null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural="Profile Table"


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    



class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    videos = models.FileField(upload_to='videos/')
    images = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__(self):
        return self.title
class Comment(models.Model):
    comment = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)

    def __ste__(self):
        return self.comment[:30]