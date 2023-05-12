from django.urls import path
from App1 import views


urlpatterns = [
    
    path('',views.inicio,name="Inicio"),
    path('kobe',views.kobe,name="kobe"),
    
]
