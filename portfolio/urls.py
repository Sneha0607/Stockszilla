from django.urls import path
from . import views

app_name="portfolio"
urlpatterns=[
path('buystocks<str:symbol>/',views.buy_stocks,name='buy_stocks'),
path('buy<str:symbol>/',views.buy,name='buy'),
path('buy<str:symbol>/<int:quantity>/',views.buy_share,name='buy_share'),
path('<str:symbol>/',views.cancel,name='cancel'),
path('records/',views.transactions,name='transaction'),
]