from django.urls import path
from . import views

urlpatterns=[
path('',views.stocks,name="stocks"),
path('company/',views.company,name='company'),
path('<str:symbol>',views.company_stocks,name='company_stocks'),
]