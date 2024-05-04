
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='home'),
   # path('login/', views.login_user,name='login'),
    path('logout_User/', views.logoutUser,name='logout_User'),
    path('register_User/', views.registertUser,name='register_User'),
    path('user_Records/<int:pk>', views.userRecords,name='user_Records'),
    path('delete_Record/<int:pk>', views.deleteRecord,name='delete_Record'),
    path('add_Record/', views.addRecord,name='add_Record'),
    path('update_Record/<int:pk>', views.updateRecord,name='update_Record'),
]