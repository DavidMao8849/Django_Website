from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:membered>/', views.member_detail, name='member_detail'),
    path('<int:membered>/friend/', views.friend_list, name='friend_list'),
]
