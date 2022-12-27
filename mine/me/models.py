from django.db import models

# Create your models here.

class user(models.Model):

    name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class usercreate(models.Model):
    username=models.CharField(max_length=100,null=True)
    Email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.username

class login2(models.Model):
    username=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
