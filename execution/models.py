from django.db import models
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User

'''
class User(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=40, primary_key=True)
    def __str__(self):
        return self.user_name
'''


class Tag(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.name


class Data(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField( null=True, blank=True)
    blog_text = models.CharField(max_length=500, null=True, blank=True)
    blog_title = models.CharField(max_length=100, null=True, blank=True)
    flag = models.BooleanField(default=False)

    def __str__(self):
         return self.blog_title


class Tag_Post(models.Model):
    user_tag = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tag_mod = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    data_mod = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, blank=True)

























