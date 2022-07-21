from django.db import models
from django.conf import settings
# Create your models here.
class loginfo(models.Model):
    email = models.EmailField(max_length=254)
    uname = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    unique_code = models.BigIntegerField()
    user_key = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.email)+" "+str(self.uname)+" "+str(self.address)+" "+str(self.city)+" "+str(self.user_key)+" "+str(self.unique_code)