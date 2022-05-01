from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

	gen = [
        ('m','Male'),
        ('f','Female'),
    ]
	
	ctry = [
        ('Australia','Australia'),
        ('Bangladesh','Bangladesh'),
        ('Brazil','Brazil'),
        ('Canada','Canada'),
        ('China','China'),
        ('France','France'),
        ('Germany','Germany'),
        ('India','India'),
        ('Italy','Italy'),
        ('Mexico','Mexico'),
        ('Pakistan','Pakistan'),
        ('Spain','Spain'),
        ('Tunisia','Tunisia'),
        ('United Kingdom','United Kingdom'),
        ('United States','United States'),
        ('Other','Other'),
    ]

	stt = [
        ("Bachelor's","Bachelor's"),
        ("Doctorate","Doctorate"),
        ("Master's","Master's"),
        ("Secondary","Secondary"),
    ]

	YoB = models.DateField("Year of Birth (yyyy-mm-dd)",auto_now_add=False, auto_now=False, blank=True, null=True)
	gender = models.CharField(max_length=30,blank=True, null=True, choices=gen)
	country = models.CharField(max_length=30,blank=True, null=True, choices=ctry)
	state = models.CharField(max_length=30,blank=True, null=True, choices=stt)
	is_teacher = models.BooleanField('Is Teacher', default=False)
	is_student = models.BooleanField('Is Student', default=False)

"""class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatar/', default='avatar_1.png')
	featured = models.BooleanField(default=False)
	is_teacher=models.BooleanField(default=False)
	joined_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(f"{self.user.username}")"""






