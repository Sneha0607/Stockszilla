from django.db import models
from django.contrib.auth.models import User

class Fund(models.Model):
	funds = models.DecimalField(max_digits=20,decimal_places=2)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
