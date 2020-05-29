from django.urls import path
from homepage_app import views

urlpatterns = [
    path('index/',views.index,name='index'),
]