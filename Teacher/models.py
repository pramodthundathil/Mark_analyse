from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    bookname = models.CharField(max_length=20)
    auther = models.CharField(max_length=20)
    options = (("IT","IT"),("CS","CS"),("MEC","MEC"),("Civil","Civil"),("Electronics","Electronics"),("Other","Other"))
    strem = models.CharField(max_length=255,choices=options)
    descrioption = models.CharField(max_length=100)
    referencelink = models.CharField(max_length=100)
    book_image = models.FileField(upload_to="book_images")
    creator = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.bookname + " by " + self.auther + " for " + "Btech " +self.strem)

class Recomendations(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    recommendation = models.TextField(max_length=2000)
    book = models.ForeignKey(Books,on_delete=models.SET_NULL,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    student_Repaly = models.CharField(max_length=255,null=True)
    Teacher = models.CharField(max_length=255,null=True)
    
    
