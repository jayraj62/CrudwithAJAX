from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Userinfo(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    hobbies=models.CharField(max_length=25)
    occupation=models.CharField(max_length=25)
    image=models.ImageField(upload_to='image')