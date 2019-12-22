from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets,permissions
from .serializers import Event_alertSerializer
from .models import Event_alert
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
# def event(request):
#     return render(request, 'eventalert/table.html', {'title': 'Event Alert'})
class Event_AlertView(LoginRequiredMixin,ListView):
    model=Event_alert
    template_name='eventalert/table.html'
    context_object_name = 'events'
    paginate_by=10
    def get_queryset(self):
        return Event_alert.objects.select_related('ackby').filter(ackby_id__isnull=True).order_by('-ackby_id','-created_at')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)      
        
    #     context['title']="Event Alert"
    #     context['events'] = Event_alert.objects.select_related('ackby').filter(ackby_id__isnull=True).order_by('-ackby_id','-created_at')
    #     return context

class Event_AlertView_Ack(LoginRequiredMixin,ListView):
    model=Event_alert
    template_name='eventalert/table.html'
    context_object_name = 'events'
    paginate_by=10
    def get_queryset(self):
        return Event_alert.objects.select_related('ackby').exclude(ackby_id__isnull=True).order_by('ackby_id','created_at')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     context['title']="Event Alert"
    #     context['events'] = Event_alert.objects.select_related('ackby').exclude(ackby_id__isnull=True).order_by('ackby_id','created_at')
    #     return context

class Event_AlertView_All(LoginRequiredMixin,ListView):
    model=Event_alert
    template_name='eventalert/table.html'
    context_object_name = 'events'
    paginate_by=10
    def get_queryset(self):
        return Event_alert.objects.select_related('ackby').order_by('-created_at')

    
class Update_isIncident(View):
    def get(self,request):
        id1 = request.GET.get('id',None)
        isIncident1 = request.GET.get('isincident',None)
        ackby1 = request.user.id
        

        obj = Event_alert.objects.get(id=id1)
        obj.is_incident = isIncident1
        obj.ackby_id = ackby1
        obj.save()

        event = {'id':obj.id}

        data = {
            'event': event
        }
        return JsonResponse(data)

class Update_Memo(View):
    def get(self,request):
        id1 = request.GET.get('id',None)
        comment1 = request.GET.get('comment',None)    

        obj = Event_alert.objects.get(id=id1)
        obj.comment = comment1
        
        obj.save()

        event = {'id':obj.id}

        data = {
            'event': event
        }
        return JsonResponse(data)

###Rest api
class Event_alertViewAPI(viewsets.ModelViewSet):
    queryset = Event_alert.objects.all()
    serializer_class = Event_alertSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
