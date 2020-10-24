from django.urls import path
from .import views
from .views import signup_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view.as_view(), name='signup'),
    #  path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
