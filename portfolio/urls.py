from django.urls import path,include
from . import views

app_name="portfolio"
urlpatterns=[
path('buystocks<str:symbol>/',views.buy_stocks,name='buy_stocks'),
path('buy<str:symbol>/',views.buy,name='buy'),
path('buy<str:symbol>/<int:quantity>/',views.buy_share,name='buy_share'),
path('records/',views.transactions,name='transaction'),
path('transaction/<int:id>/',views.user_transaction,name='user_transaction'),
path('user_holdings/<str:symbol>/',views.user_holdings,name='user_holding'),
path('sell/<int:id>/',views.sell,name='sell'),
path('sell_stocks/<int:id>/',views.sell_stocks,name='sell_stocks'),
path('sell_share/<int:id>/<int:quantity>',views.sell_share,name='sell_share'),
path('holdings/',views.holdings,name='holding'),
path('<str:symbol>/',views.cancel,name='cancel'),
]

urlpatterns+=[
path('quotes',include('quotes.urls')),
]