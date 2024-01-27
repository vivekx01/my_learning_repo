from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.todoview,name='homepage'),
    path('addtask/',views.addtask),
    path('deletetask/<int:taskpk>/',views.deletetask),
    path('edittask/<int:taskpk>/',views.edittaskview),
    path('edittask/<int:taskpk>/update/',views.edittask)
]
