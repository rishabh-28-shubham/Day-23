from django.db import models

class Ch_Department(models.TextChoices):
    Human_Resource = 'HR', 'Human Resource',
    Sales = 'SL', 'Sales',
    Finance = 'FN', 'Finance',
    Technical = 'TH', 'Technical'

# Create your models here.
class Employee(models.Model):
    Emp_name = models.TextField(max_length=100)
    Emp_address = models.TextField(max_length=200)
    Emp_department = models.CharField(max_length=50 , choices=Ch_Department.choices, default = 'Sales')
    Emp_profile = models.ImageField(upload_to='emp_prf_img/')