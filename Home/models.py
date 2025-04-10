from django.db import models


from django.contrib.auth.models import User, Group

class Parent_Student_Relation(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent')
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    
    def __str__(self):
        return f"{self.parent.username} - {self.student.username}"
