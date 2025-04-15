from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('account/<str:oaccount>/', views.owner_detail, name='owner_detail'),
]