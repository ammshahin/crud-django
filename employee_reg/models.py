from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullName = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=20)
    mobileNo = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
