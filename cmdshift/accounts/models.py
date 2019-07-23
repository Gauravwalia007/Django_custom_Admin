from django.db import models

class Users(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    mobno=models.IntegerField()
    image=models.ImageField(upload_to ='pics')
