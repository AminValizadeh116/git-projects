from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

app_name = 'social'

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
]
