from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	username=models.ForeignKey(User,default=None,on_delete=models.CASCADE)

	def __str__(self):
		return self.ticker