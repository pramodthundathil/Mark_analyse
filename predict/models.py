from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Datamodel(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    btech_branch = models.CharField(max_length=10)
    physics_10 = models.FloatField()
    chemistry_10 = models.FloatField()
    maths_10 = models.FloatField()
    physics_12 = models.FloatField()
    chemistry_12 = models.FloatField()
    maths_12 = models.FloatField()
    btech_sem1 = models.FloatField()
    btech_sem2 = models.FloatField()
    btech_sem3 = models.FloatField()
    btech_sem4 = models.FloatField()
    mode_study = models.CharField(max_length=10)
    study_time = models.FloatField()
    prediction_result = models.CharField(max_length=255,null=True,blank=True)
    attendance = models.FloatField(null=True,blank=True)
    iq_marks = models.FloatField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class Question(models.Model):
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    img = models.FileField(upload_to='quesimg')
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

    def __str__(self):
        return self.question
    
# class Result(models.Mode):
#     Question=models.ForeignKey(Question,on_delete=models.SET_NULL,null=True)
    
    
    
    
class Examination(models.Model):
    exam_name = models.CharField(max_length=100)
    exam_date = models.DateField()
    def __str__(self):
        return str(self.exam_name + " " + str(self.exam_date))
    

class mark_exams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_mark')
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name='exam')
    subject = models.CharField(max_length=100 )
    marks = models.FloatField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.user.username + " " + self.subject + " " + str(self.marks) + " " + str(self.date))
