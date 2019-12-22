from django.urls import path 
from . import views

app_name='budget'

urlpatterns = [    
    path("",views.project_list,name="list"),
    path("<slug:project_slug>",views.project_detail,name="detail")    
]