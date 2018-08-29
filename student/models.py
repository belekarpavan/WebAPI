from django.db import models

# Create your models here.

class student(models.Model):
    roll=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.name
