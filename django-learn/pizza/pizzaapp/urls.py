from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',views.adminloginview,name='adminloginpage'),
    path('adminauthenticate/',views.authenticateadmin),
    path('admin/homepage/',views.adminhomepageview,name='adminhomepage'),
    path('adminlogout/',views.logoutadmin),
    path('addpizza/',views.addpizza),
    path('deletepizza/<int:pizzapk>/',views.deletepizza),
    path('',views.homepageview,name='homepage'),
    path('signupuser/',views.signup),
    path('userlogin/',views.userloginview,name='userlogin'),
    path('customer/welcome/',views.customerwelcomeview,name='customerpage'),
    path('customer/authenticate/',views.userauthenticate),
    path('userlogout/',views.logoutuser),
    path('placeorder/',views.placeorder),
    path('myorders/',views.userorders),
    path('receivedorders/',views.adminorders),
    path('acceptorder/<int:orderpk>/',views.acceptorder),
    path('deleteorder/<int:orderpk>/',views.declineorder)
]
