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

class Data(models.Model):
#    username = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateField(auto_now=True)
    pub_date = models.DateField(null=True, blank=True)
    blog_text = models.CharField(max_length=500, null=True, blank=True)
    blog_title = models.CharField(max_length=500, null=True, blank=True)
    flag = models.BooleanField(default=False)


































