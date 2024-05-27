from django.db import models

# Create your models here.
class activity (models.Model):
    username=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
class act (models.Model):
    npassword=models.CharField(max_length=50)
    cpassword=models.CharField(max_length=50)


