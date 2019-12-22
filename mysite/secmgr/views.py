from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.http import JsonResponse
from rest_framework import viewsets,permissions
from .serializers import ScanTasksSerializer
from .models import ScanSchedule

class ScanScheduleView(TemplateView):
    # model = ScanSchedule
    template_name='secmgr/taskscan.html'
    # context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = ScanSchedule.objects.all()
        return context

class CreateScanTask(View):
    def get(self, request):
        app1 = request.GET.get('appname', None)
        task1 = request.GET.get('taskscan', None)        

        obj = ScanSchedule.objects.create(
            appname = app1,
            taskscan = task1
        )

        task = {'id':obj.id,'appname':obj.appname,'taskscan':obj.taskscan}

        data = {
            'task': task
        }
        return JsonResponse(data)

class DeleteScanTask(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        ScanSchedule.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class UpdateScanTask(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        app1 = request.GET.get('appname', None)
        task1 = request.GET.get('taskscan', None)
        

        obj = ScanSchedule.objects.get(id=id1)
        obj.appname = app1
        obj.taskscan = task1        
        obj.save()

        task = {'id':obj.id,'appname':obj.appname,'taskscan':obj.taskscan}

        data = {
            'task': task
        }
        return JsonResponse(data)

##Rest api
class ScanScheduleViewAPI(viewsets.ModelViewSet):
    queryset = ScanSchedule.objects.all()
    serializer_class = ScanTasksSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
