from django.db import models


class employe(models.Model):
    name=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    emp_id=models.IntegerField(unique=True,blank=False)
    location=models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
# Create your models here.

class author(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):

        return self.title
    

class test(models.Model):
    first=models.CharField(max_length=100)
    last=models.CharField(max_length=100)
    auth=models.ForeignKey(author,on_delete=models.CASCADE)

    def __str__(self):
        return self.first



class Address(models.Model):
    city=models.CharField(max_length=100)
    def __str__(Self):
        return Self.city
class detail(models.Model):
    first=models.CharField(max_length=100)
    last=models.CharField(max_length=100)
    ad=models.OneToOneField(Address,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first


class published(models.Model):
    country=models.CharField(max_length=100)
    code=models.CharField(max_length=2)

    def __str__(self):

        return self.country


class Bookname(models.Model):
    titel=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pub_count=models.ManyToManyField(published)

    def __str__(self):
        return self.titel



