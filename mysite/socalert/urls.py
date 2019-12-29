from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('eventalert',views.Event_alertViewAPI)
router.register('geteventrule',views.Event_getRuleViewAPI)



urlpatterns = [
    path('',include(router.urls)),
    # path('eventalert/',views.Event_AlertView.as_view(), name='socalert-eventalert'),
    # path(r'^open/$', views.Event_AlertView.as_view(), name='open'),
]
