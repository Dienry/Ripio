from django.urls import path

from . import views

app_name = 'coinapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_coin/', views.create_coin, name='create_coin'),
    path('balance/<str:user_name>/', views.balance, name='balance'),
    path('send_money/', views.send_money, name='send_money'),
    path('save_coin/', views.save_coin, name='save_coin'),
    path('make_transfer/', views.make_transfer, name='make_transfer'),
    path('movements/<str:user_name>/', views.movements, name='movements'),
]