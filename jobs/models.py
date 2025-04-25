from django.db import models

# Create your models here.
class Job(models.Model):
    company=models.CharField(max_length=100)
    role=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100)
    description=models.TextField()
    experience=models.CharField(max_length=50)
    skills_required=models.CharField(max_length=100)
    salary=models.IntegerField()
    hr=models.CharField(max_length=50)