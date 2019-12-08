from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('vatasks',views.ScanScheduleViewAPI)
router.register('vatasks2',views.ScanScheduleViewAPI)

urlpatterns = [
   path('',include(router.urls)) 
]