from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	is_admin= models.BooleanField('Is admin', default=False)
	is_customer = models.BooleanField('Is customer', default=False)
	is_employee = models.BooleanField('Is employee', default=False)
"""class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatar/', default='avatar_1.png')
	featured = models.BooleanField(default=False)
	is_teacher=models.BooleanField(default=False)
	joined_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(f"{self.user.username}")"""






