from django.urls import path
from addition_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add')
]