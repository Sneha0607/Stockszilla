from django.shortcuts import render
from .models import Stock
from django.http import JsonResponse

def stocks(request):
	import requests
	import json
	api_req1=requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_req2=requests.get("https://cloud.iexapis.com/stable/stock/googl/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_req3=requests.get("https://cloud.iexapis.com/stable/stock/amzn/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_req4=requests.get("https://cloud.iexapis.com/stable/stock/ibm/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_req5=requests.get("https://cloud.iexapis.com/stable/stock/fb/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_req6=requests.get("https://cloud.iexapis.com/stable/stock/tcs/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_req7=requests.get("https://cloud.iexapis.com/stable/stock/wit/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_req8=requests.get("https://cloud.iexapis.com/stable/stock/infy/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_req9=requests.get("https://cloud.iexapis.com/stable/stock/msft/quote?token=pk_5809718036484b32b2511b568e7ed15a")
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
	apis=[api1,api2,api3,api4,api5,api6,api7,api8,api9
	]

	return render(request,'companystocks.html',{'apis':apis})



def company(request):
	import requests
	import json
	h_var='Time'
	v_var='Price'
	title='Time vs Price(Last 20 minutes)'
	dates=[[h_var,v_var]]
	ticker= request.POST['ticker']
	
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker + "/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_chartreq=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/chart/1d?token=pk_5809718036484b32b2511b568e7ed15a")
	
	
	try:
		api=json.loads(api_req.content)
		
		
	except Exception as e:
		api="Error..."

	try:
		api_chart=json.loads(api_chartreq.content)
		

	except Exception as e:
		api_chart="Error..."
	dates_JSON="Error.."

	for api_c in api_chart:
		dates.append([api_c['minute'],api_c['close']])
	h_var_JSON=json.dumps(h_var)
	v_var_JSON=json.dumps(v_var)
	dates_JSON=json.dumps(dates)
	title_JSON=json.dumps(title)

	return render(request,'company.html',{'api':api,'dates_JSON':dates_JSON,'h_var_JSON':h_var_JSON,'v_var_JSON':v_var_JSON,'title_JSON':title_JSON})

def company_stocks(request,symbol):
	import requests
	import json
	h_var='Time'
	v_var='Price'
	title='Time vs Price(last 20 minutes)'
	dates=[[h_var,v_var]]
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ symbol + "/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	api_chartreq=requests.get("https://cloud.iexapis.com/stable/stock/"+ symbol +"/chart/1d?token=pk_5809718036484b32b2511b568e7ed15a")
	try:
		api=json.loads(api_req.content)
		
			
	except Exception as e:
		api="Error..."

	try:
		api_chart=json.loads(api_chartreq.content)
		for api_c in api_chart:
			dates.append([api_c['minute'],api_c['close']])
		h_var_JSON=json.dumps(h_var)
		v_var_JSON=json.dumps(v_var)
		dates_JSON=json.dumps(dates)
		title_JSON=json.dumps(title)

	except Exception as e:
		api_chart="Error..."
		dates_JSON="Error..."
	
	return render(request,'company.html',{'api':api,'dates_JSON':dates_JSON,'h_var_JSON':h_var_JSON,'v_var_JSON':v_var_JSON,'title_JSON':title_JSON})

def graph(request,ticker):
	import requests
	import json
	h_var=''
	v_var=''
	dates=[[h_var,v_var]]
	
	g_type=request.POST.get('g_type',False);
	g_scale=request.POST.get('g_scale',False);
	api_req=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker + "/quote?token=pk_5809718036484b32b2511b568e7ed15a")
	
	
	try:
		api=json.loads(api_req.content)
		
		
	except Exception as e:
		api="Error..."

	if(g_scale == "1"):
		h_var='Date'
		v_var='Close price'
		title='Day vs Close price(1 year)'
		try:
			api_chartreq=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/chart/1y?token=pk_5809718036484b32b2511b568e7ed15a")
			api_chart=json.loads(api_chartreq.content)
			for api_c in api_chart:
				dates.append([api_c['date'],api_c['close']])
			h_var_JSON=json.dumps(h_var)
			v_var_JSON=json.dumps(v_var)
			dates_JSON=json.dumps(dates)
			title_JSON=json.dumps(title)


		except Exception as e:
			api_chart="Error..."
			dates_JSON="Error..."

	elif(g_scale == "2"):
		h_var='Date'
		v_var='Close price'
		title='Day vs Close price(1 month)'
		try:
			api_chartreq=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/chart/1m?token=pk_5809718036484b32b2511b568e7ed15a")
			api_chart=json.loads(api_chartreq.content)
			for api_c in api_chart:
				dates.append([api_c['date'],api_c['close']])
			h_var_JSON=json.dumps(h_var)
			v_var_JSON=json.dumps(v_var)
			dates_JSON=json.dumps(dates)
			title_JSON=json.dumps(title)


		except Exception as e:
			api_chart="Error..."
			dates_JSON="Error..."

	

	elif(g_scale == "4"):
		h_var='Time'
		v_var='Price'
		title='Time vs Price(1 day)'
		try:
			api_chartreq=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/chart/1d?token=pk_5809718036484b32b2511b568e7ed15a")
			api_chart=json.loads(api_chartreq.content)
			for api_c in api_chart:
				if(api_c['minute']=='00:00' or api_c['minute']=='01:00' or api_c['minute']=='02:00' or api_c['minute']=='03:00' or api_c['minute']=='04:00' or api_c['minute']=='05:00' or api_c['minute']=='06:00' or api_c['minute']=='07:00' or api_c['minute']=='08:00' or api_c['minute']=='09:00' or api_c['minute']=='10:00' or api_c['minute']=='11:00' or api_c['minute']=='12:00' or api_c['minute']=='13:00' or api_c['minute']=='14:00' or api_c['minute']=='15:00' or api_c['minute']=='16:00' or api_c['minute']=='17:00' or api_c['minute']=='18:00' or api_c['minute']=='19:00' or api_c['minute']=='20:00' or api_c['minute']=='21:00' or api_c['minute']=='22:00' or api_c['minute']=='23:00'):
					dates.append([api_c['minute'],api_c['close']])
			h_var_JSON=json.dumps(h_var)
			v_var_JSON=json.dumps(v_var)
			dates_JSON=json.dumps(dates)
			title_JSON=json.dumps(title)


		except Exception as e:
			api_chart="Error..."
			dates_JSON="Error..."

	elif(g_scale == "5"):
		h_var='Time'
		v_var='Price'
		title='Time vs Price(Last 20 minutes)'
		try:
			api_chartreq=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/intraday-prices?&chartLast=20&token=pk_5809718036484b32b2511b568e7ed15a")
			api_chart=json.loads(api_chartreq.content)
			for api_c in api_chart:
				dates.append([api_c['minute'],api_c['close']])
			h_var_JSON=json.dumps(h_var)
			v_var_JSON=json.dumps(v_var)
			dates_JSON=json.dumps(dates)
			title_JSON=json.dumps(title)


		except Exception as e:
			api_chart="Error..."
			dates_JSON="Error..."


	else:
		h_var='Time'
		v_var='Price'
		title='Time vs Price(by minute)'
		try:
			api_chartreq=requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/chart/1d?token=pk_5809718036484b32b2511b568e7ed15a")
			api_chart=json.loads(api_chartreq.content)
			for api_c in api_chart:
				dates.append([api_c['minute'],api_c['close']])
			h_var_JSON=json.dumps(h_var)
			v_var_JSON=json.dumps(v_var)
			dates_JSON=json.dumps(dates)
			title_JSON=json.dumps(title)


		except Exception as e:
			api_chart="Error..."
			dates_JSON="Error..."


   
		

	return render(request,'graph.html',{'api':api,'dates_JSON':dates_JSON,'g_type':g_type})