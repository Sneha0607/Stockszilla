from django.shortcuts import render,redirect
import requests
import json
from accounts.models import Fund
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Transaction,Holding
from quotes.views import company_stocks

# Create your views here.
def buy_stocks(request,symbol):
	a=Fund.objects.get(user=request.user)
	money=a.funds
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ symbol + "/quote?token=pk_80042db83f9d49fc8195b96daf7a75ec")
	try:
		api=json.loads(api_req.content)
		
			
	except Exception as e:
		api="Error..."

	return render(request, 'buystocks.html', {'api':api,'money':money})

def buy(request,symbol):
	a=Fund.objects.get(user=request.user)
	money=a.funds
	q=request.POST.get('quantity')
	if (not q):
		q=0
	quantity=int(q)
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ symbol + "/quote?token=pk_80042db83f9d49fc8195b96daf7a75ec")
	try:
		api=json.loads(api_req.content)
		
			
	except Exception as e:
		api="Error..."

	if (api=="Error..."):
		price=0.0
		t_price=0.0
		c_balance=money

	else:
		price=api['latestPrice']
		t_price=quantity*price
		c_balance=float(money)-t_price

	

	if((quantity == 0) or (quantity < 0) or (c_balance < 0)):
		messages.error(request,'Enter valid no. of shares')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	return render(request, 'buy.html', {'quantity':quantity,'price':price,'api':api,'t_price':t_price,'c_balance':c_balance,'money':money})
	
def transactions(request):
	a=Fund.objects.get(user=request.user)
	money = a.funds
	t = Transaction.objects.filter(user=request.user)
	if (t.exists()):
		b="1"
	else:
		b="0"
	return render(request, 'transactions.html', {})

def buy_share(request,symbol,quantity):
	b=Fund.objects.get(user=request.user)
	money = b.funds
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ symbol + "/quote?token=pk_80042db83f9d49fc8195b96daf7a75ec")
	try:
		api=json.loads(api_req.content)
		
			
	except Exception as e:
		api="Error..."

	if (api=="Error..."):
		return buy_stocks(request,symbol)

	price=api['latestPrice']
	t_price=quantity*price
	c_balance=float(money)-t_price
	company=api['companyName']
	newtransaction=Transaction(user=request.user,company=company,price_per_share=price,total_price=t_price,action="bought",b_balance=money,a_balance=c_balance,symbol=symbol,quantity=quantity)
	newtransaction.save()
	newholding=Holding(user=request.user,company=company,price_per_share=price,total_price=t_price,symbol=symbol,quantity=quantity)
	newholding.save()
	a=Fund.objects.get(user=request.user)
	a.funds=c_balance
	a.save()
	return company_stocks(request,symbol)

def cancel(request,symbol):
	return company_stocks(request,symbol)

