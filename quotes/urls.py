from django.urls import path
from . import views

urlpatterns=[
path('',views.stocks,name="stocks"),
path('company/',views.company,name="company"),
path('company/<str:ticker>',views.graph,name="graph"),
path('<str:symbol>',views.company_stocks,name='company_stocks'),
path('Add_to_favourites/<str:symbol>',views.add_to_favourites,name='favourites'),
path('favourites/',views.fav,name='fav'),
]