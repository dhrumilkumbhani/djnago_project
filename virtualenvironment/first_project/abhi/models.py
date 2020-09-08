from __future__ import unicode_literals  #meta class add karva add kro
from django.db import models
# Create your models here.
class  employee1(models.Model):
	f_name=models.CharField(max_length=100)
	l_name=models.CharField(max_length=100)
	email=models.EmailField()
	mobilenumber=models.IntegerField()
	gender=models.BooleanField()
	birth_date=models.DateTimeField()
	def __str__(self):
		return self.email
	class Meta:
		db_table = "employee1"  


class student(models.Model):  
    firstname = models.CharField(max_length=50)  
    lastname  = models.CharField(max_length = 100)
    mobile = models.IntegerField()
    date = models.DateTimeField()
    file =models.FileField()
