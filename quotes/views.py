from django.shortcuts import render
from .models import Stock

def stocks(request):
	import requests
	import json
	api_req1=requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req2=requests.get("https://cloud.iexapis.com/stable/stock/googl/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req3=requests.get("https://cloud.iexapis.com/stable/stock/amzn/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req4=requests.get("https://cloud.iexapis.com/stable/stock/ibm/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req5=requests.get("https://cloud.iexapis.com/stable/stock/fb/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req6=requests.get("https://cloud.iexapis.com/stable/stock/tcs/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req7=requests.get("https://cloud.iexapis.com/stable/stock/wit/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req8=requests.get("https://cloud.iexapis.com/stable/stock/infy/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req9=requests.get("https://cloud.iexapis.com/stable/stock/msft/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req10=requests.get("https://cloud.iexapis.com/stable/stock/yhoo/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req11=requests.get("https://cloud.iexapis.com/stable/stock/orcl/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	api_req12=requests.get("https://cloud.iexapis.com/stable/stock/gs/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	try:
		api1=json.loads(api_req1.content)
	except Exception as e:
		api1="Error..."
	try:
		api2=json.loads(api_req2.content)
	except Exception as e:
		api2="Error..."
	try:
		api3=json.loads(api_req3.content)
	except Exception as e:
		api3="Error..."
	try:
		api4=json.loads(api_req4.content)
	except Exception as e:
		api4="Error..."
	try:
		api5=json.loads(api_req5.content)
	except Exception as e:
		api5="Error..."
	try:
		api6=json.loads(api_req6.content)
	except Exception as e:
		api6="Error..."
	try:
		api7=json.loads(api_req7.content)
	except Exception as e:
		api7="Error..."
	try:
		api8=json.loads(api_req8.content)
	except Exception as e:
		api8="Error..."
	try:
		api9=json.loads(api_req9.content)
	except Exception as e:
		api9="Error..."
	try:
		api10=json.loads(api_req10.content)
	except Exception as e:
		api10="Error..."
	try:
		api11=json.loads(api_req11.content)
	except Exception as e:
		api11="Error..."
	try:
		api12=json.loads(api_req12.content)
	except Exception as e:
		api12="Error..."
	apis=[api1,api2,api3,api4,api5,api6,api7,api8,api9,api10,api11,api12
	]

	return render(request,'companystocks.html',{'apis':apis})



def company(request):
	import requests
	import json

	ticker= request.POST['ticker']
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker + "/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	try:
		api=json.loads(api_req.content)
	except Exception as e:
		api="Error..."
	return render(request,'company.html',{'api':api})

def company_stocks(request,symbol):
	import requests
	import json
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ symbol + "/quote?token=pk_c1f4ae05dcbb4efab4ed0cb819030614")
	try:
		api=json.loads(api_req.content)
	except Exception as e:
		api="Error..."
	return render(request,'company.html',{'api':api})