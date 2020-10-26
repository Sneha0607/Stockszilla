from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('accounts/', include('accounts.urls')),
    path('quotes/',include('quotes.urls')),
]

urlpatterns+=[
path('portfolio',include('portfolio.urls',namespace='portfolio')),
]
urlpatterns += staticfiles_urlpatterns()
