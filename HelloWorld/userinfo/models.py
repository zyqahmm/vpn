from django.db import models
 
class userinfo(models.Model):
    Mail = models.CharField(max_length=20)
    Phone = models.CharField(max_length=11)