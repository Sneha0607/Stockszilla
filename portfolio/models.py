from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
	user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	company = models.CharField(max_length=100)
	price_per_share = models.DecimalField(max_digits=20,decimal_places=2)
	total_price = models.DecimalField(max_digits=20,decimal_places=2)
	action = models.CharField(max_length=5)
	gain_loss = models.CharField(max_length=5,null=True)
	amount = models.DecimalField(max_digits=20,decimal_places=2,null=True)
	b_balance = models.DecimalField(max_digits=20,decimal_places=2)
	a_balance = models.DecimalField(max_digits=20,decimal_places=2)
	symbol = models.CharField(max_length=10)
	quantity = models.IntegerField()
	date = models.DateField(auto_now=True)

class Holding(models.Model):
	user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	company = models.CharField(max_length=100)
	price_per_share = models.DecimalField(max_digits=20,decimal_places=2)
	total_price = models.DecimalField(max_digits=20,decimal_places=2)
	symbol = models.CharField(max_length=10)
	quantity = models.IntegerField()


