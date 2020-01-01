from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,re_path,include
from django.conf.urls import url

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from programming import views as programming_views
from core import views as core_views
from secmgr import views as secmgr_views
from socalert import views as socalert_views

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
    # path('api/token/', obtain_auth_token, name='obtain-token'),
    path('tinymce',include('tinymce.urls')),
    path('secmgr/taskscan/',secmgr_views.ScanScheduleView.as_view(),name='secmgr-taskscan'),
    path('secmgr/taskscan/create/',secmgr_views.CreateScanTask.as_view(), name='secmgr-taskscan_create'),
    path('secmgr/taskscan/update/',secmgr_views.UpdateScanTask.as_view(), name='secmgr-taskscan_update'),
    path('secmgr/taskscan/delete/',secmgr_views.DeleteScanTask.as_view(), name='secmgr-taskscan_delete'),
    path('secmgr_api/',include('secmgr.urls')),

    ###eventalert
    path('socalert_api/',include('socalert.urls')),    
    path('socalert/eventalert/',socalert_views.Event_AlertView.as_view(), name='socalert-eventalert'),
    path('socalert/eventalert/tab_ack/',socalert_views.Event_AlertView_Ack.as_view(), name='socalert-eventack'),
    path('socalert/eventalert/tab_all/',socalert_views.Event_AlertView_All.as_view(), name='socalert-eventall'),
    path('socalert/eventalert/tab_incidents/',socalert_views.Event_IncidentsView.as_view(),name='socalert-incidents'),
    path('socalert/eventalert/ack_update/',socalert_views.Update_isIncident.as_view(),name='socalert-ack_update'),
    path('socalert/eventalert/memo_update/',socalert_views.Update_Memo.as_view(),name='socalert-memo_update'),
    path('socalert/eventalert/close_event/',socalert_views.Closed_Event.as_view(),name='socalert-closed_event'),
    
    ###eventrule
    path('socalert/eventrule/',socalert_views.Event_RulesView.as_view(), name='socalert-eventrule'),
    path('socalert/eventruledetail/',socalert_views.Event_Rule_Detail.as_view(), name='socalert-eventruledetail'),
    path('socalert/eventrule/new/',socalert_views.Event_Rule_CreateView.as_view(),name='socalert-createrule'),
    path('socalert/eventrule/<int:pk>/update/', socalert_views.Event_Rule_UpdateView.as_view(), name='socalert-ruleupdate'),

    path('api-auth/',include('rest_framework.urls')),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
