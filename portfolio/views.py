from django.shortcuts import render,redirect
import requests
import json
from accounts.models import Fund
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Transaction,Holding
from quotes.views import company_stocks
from django.urls import reverse

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
	return render(request, 'transactions.html', {'money':money,'b':b,'t':t})

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
	return redirect('portfolio:transaction')

def cancel(request,symbol):
	return redirect(reverse('company_stocks',kwargs={'symbol':symbol}))

def user_transaction(request,id):
	b=Fund.objects.get(user=request.user)
	money = b.funds
	t = Transaction.objects.get(id=id)
	return render(request,'user_transaction.html',{'money':money,'t':t})

def holdings(request):
	b=Fund.objects.get(user=request.user)
	money = b.funds
	t = Holding.objects.filter(user=request.user)
	if (t.exists()):
		b="1"
	else:
		b="0"
	return render(request,'holdings.html',{'money':money,'t':t,'b':b})

def user_holdings(request,symbol):
	b=Fund.objects.get(user=request.user)
	money = b.funds
	t = Holding.objects.filter(user=request.user,symbol=symbol)
	return render(request,'holdings.html',{'money':money,'t':t})

def sell(request,id):
	b=Fund.objects.get(user=request.user)
	money = b.funds
	h=Holding.objects.get(id=id)
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ str(h.symbol) + "/quote?token=pk_80042db83f9d49fc8195b96daf7a75ec")
	try:
		api=json.loads(api_req.content)
		
	except Exception as e:
		api="Error..."
	if(api=="Error..."):
		price=0
	else:
		price=api['latestPrice']
	return render(request,'sell.html',{'h':h,'price':price,'api':api,'money':money})

def sell_stocks(request,id):
	b=Fund.objects.get(user=request.user)
	money = b.funds
	q=request.POST.get('quantity')
	if (not q):
		q=0
	quantity=int(q)
	h=Holding.objects.get(id=id)
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ str(h.symbol) + "/quote?token=pk_80042db83f9d49fc8195b96daf7a75ec")
	try:
		api=json.loads(api_req.content)
		
			
	except Exception as e:
		api="Error..."

	if (api=="Error..."):
		price=0.0
		t_price=0.0
		c_balance=money
		g_l=""
		amt=0.0

	else:
		price=api['latestPrice']
		t_price=quantity*price
		c_balance=float(money)+t_price
		amt=t_price-float(h.price_per_share)*quantity
		if(amt < 0):
			amt=0-amt
			g_l="Loss"
		else:
			g_l="Profit"

	if((quantity == 0) or (quantity < 0) or (quantity > h.quantity)):
		messages.error(request,'Enter valid no. of shares')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	return render(request,'sell_stocks.html',{'api':api,'money':money,'h':h,'quantity':quantity,'price':price,'t_price':t_price,'c_balance':c_balance,'amt':amt,'g_l':g_l})

def sell_share(request,id,quantity):
	b=Fund.objects.get(user=request.user)
	money = b.funds
	h=Holding.objects.get(id=id)
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ str(h.symbol) + "/quote?token=pk_80042db83f9d49fc8195b96daf7a75ec")
	try:
		api=json.loads(api_req.content)
		
	except Exception as e:
		api="Error..."

	if (api=="Error..."):
		return buy_stocks(request,symbol)

	price=api['latestPrice']
	t_price=quantity*price
	c_balance=float(money)+t_price
	company=h.company
	amt=t_price-float(h.price_per_share)*quantity
	if(amt < 0):
		amt=0-amt
		g_l="Loss"
	else:
		g_l="Profit"
	newtransaction=Transaction(user=request.user,company=company,price_per_share=price,total_price=t_price,action="sold",b_balance=money,a_balance=c_balance,symbol=h.symbol,quantity=quantity,amount=amt,gain_loss=g_l)
	newtransaction.save()
	if(quantity-h.quantity == 0):
		h.delete()
	else:
		h.quantity=h.quantity-quantity
		h.save()
	a=Fund.objects.get(user=request.user)
	a.funds=c_balance
	a.save()
	return redirect('portfolio:transaction')




