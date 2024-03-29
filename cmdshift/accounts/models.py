from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    city=models.CharField(max_length=100)
    image=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username



    def create_user(sender,**kwargs):
        if kwargs['created']:
            user_profile=UserProfile.objects.create(user=kwargs['instance'])


    post_save.connect(create_user,sender=User)

