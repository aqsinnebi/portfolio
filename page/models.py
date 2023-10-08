from django.db import models


class Home(models.Model):
    title= models.CharField(max_length=20)
    txt1 =models.CharField(max_length=20)
    txt2 =models.CharField(max_length=20)
    img= models.ImageField(upload_to='picture')
    update= models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    name= models.CharField(max_length=20)
    prof= models.CharField(max_length=20)
    desc= models.TextField(blank=False)
    img= models.ImageField(upload_to='about')
    update= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Skills(models.Model):
    name= models.CharField(max_length=40)
    update= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Contact(models.Model):
    email= models.CharField(max_length=40)
    phone= models.CharField(max_length=20)
    adres= models.CharField(max_length=200)
    update= models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    
    
    
# Create your models here.
