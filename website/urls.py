
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='home'),
   # path('login/', views.login_user,name='login'),
    path('logout_User/', views.logoutUser,name='logout_User'),
]