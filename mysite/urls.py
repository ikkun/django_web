"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include

from rest_framework.authtoken.views import obtain_auth_token

from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from programming import views as programming_views
from core import views as core_views
from secmgr import views as secmgr_views

urlpatterns = [
    path('', include('blog.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('programming/',programming_views.authors,name='authors'),
    path('framework/',programming_views.framework,name='framework'),
    path('download/',programming_views.download_csv,name='download_csv'),
    path('budget/',include('budget.urls')),
    path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
    path('blog-register/',user_views.register,name='register'),
    path('blog-profile/',user_views.profile,name='profile'),
    path('blog-login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('blog-logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    # path('core/',core_views.PostView.as_vie
    # w(),name='test'),
    path('core/create/',core_views.PostCreateView.as_view(),name='rest-create'),
    path('core/list-create/',core_views.PostCreateView.as_view(),name='rest-listcreate'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('tinymce',include('tinymce.urls')),
    path('secmgr/taskscan/',secmgr_views.ScanScheduleView.as_view(),name='secmgr-taskscan'),
    path('secmgr/taskscan/create/',secmgr_views.CreateScanTask.as_view(), name='secmgr-taskscan_create'),
    path('secmgr/taskscan/update/',secmgr_views.UpdateScanTask.as_view(), name='secmgr-taskscan_update'),
    path('secmgr/taskscan/delete/',secmgr_views.DeleteScanTask.as_view(), name='secmgr-taskscan_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
