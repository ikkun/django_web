from django.urls import path 
from . import views

app_name='programming'

urlpatterns = [    
    path("",views.authors,name="authors"),    
]