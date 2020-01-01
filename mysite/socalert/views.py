from django.shortcuts import render,get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import (
    TemplateView,
    View,
    ListView,
    CreateView,
    UpdateView
)
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets,permissions

from .serializers import Event_alertSerializer,Event_ruleSerializer
from .models import Event_alert,Event_rule
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime,timedelta,timezone

# @login_required
# def event(request):
#     return render(request, 'eventalert/table.html', {'title': 'Event Alert'})
def nav_count():
    c_open = Event_alert.objects.filter(Q(analyse_by_id__isnull=True)|Q(closed_by_id__isnull=True)).count()
    c_incidents = Event_alert.objects.filter(Q(is_incident__exact=1)).count()
    
    return dict({'eventopen':c_open,'eventincident':c_incidents})

####Event rule
class Event_RulesView(LoginRequiredMixin,ListView):
    model = Event_rule
    template_name = 'eventrule/table.html'
    context_object_name = 'rules'
    ordering = ['rule']
    paginate_by = 10

class Event_Rule_CreateView(LoginRequiredMixin,CreateView):
    model = Event_rule
    template_name="eventrule/event_rule_form.html"
    success_url=reverse_lazy('socalert-eventalert')
    fields = ['rule','types','service','title','impact','urgency','contact','howto']
    def form_valid(self, form):
        form.instance.created_by_id = self.request.user.id
        form.instance.created_at = datetime.now()+timedelta(hours=7)
        return super().form_valid(form)

class Event_Rule_UpdateView(LoginRequiredMixin,UpdateView):
    model = Event_rule
    template_name = "eventrule/event_rule_form.html"
    success_url = './'
    fields = ['rule','types','service','title','impact','urgency','contact','howto']
    def form_valid(self, form):
        form.instance.updated_by_id = self.request.user.id
        form.instance.updated_at = datetime.now()+timedelta(hours=7)
        return super().form_valid(form)

class Event_Rule_Detail(View):
    def get(self,request):
        rule1 = request.GET.get('rule',None)
        obj = Event_rule.objects.get(rule=rule1)
        # isIncident1 = request.GET.get('isincident',None)
        # analyse_by1 = request.user.id    

        ruleobj = [{"rule": obj.rule, "types": obj.types,
        "title": obj.title, "impact": obj.impact, "urgency": obj.urgency, 
        "contact": obj.contact}]        
        return JsonResponse(ruleobj, status=200, safe=False,json_dumps_params={'ensure_ascii': False})

####Event alert
class Event_AlertView(LoginRequiredMixin,ListView):
    model=Event_alert
    template_name='eventalert/table.html'
    context_object_name = 'events'
    paginate_by=10
    def get_queryset(self):
        return Event_alert.objects.filter(Q(analyse_by_id__isnull=True)|Q(closed_by_id__isnull=True)).order_by('-analyse_by_id','-created_at')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title']="Event Alert-Open"        
        context.update(nav_count())  
        
        return context

class Event_IncidentsView(LoginRequiredMixin,ListView):
    model=Event_alert
    template_name='eventalert/table.html'
    context_object_name = 'events'
    paginate_by=10
    def get_queryset(self):
        return Event_alert.objects.filter(Q(is_incident__exact=1)).order_by('-analyse_by_id','-created_at')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title']="Event Alert-Incidents"        
        context.update(nav_count())  
        
        return context

class Event_AlertView_Ack(LoginRequiredMixin,ListView):
    model=Event_alert
    template_name='eventalert/table.html'
    context_object_name = 'events'
    paginate_by=10
    def get_queryset(self):
        return Event_alert.objects.exclude(Q(analyse_by_id__isnull=True)|Q(closed_by_id__isnull=True)).order_by('analyse_by_id','created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title']="Event Alert-Ackknowledge"
        context.update(nav_count()) 
        return context
        

class Event_AlertView_All(LoginRequiredMixin,ListView):
    model=Event_alert
    template_name='eventalert/table.html'
    context_object_name = 'events'
    paginate_by=10
    def get_queryset(self):
        return Event_alert.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title']="Event Alert-ALL"
        context.update(nav_count()) 
        return context


        

    
class Update_isIncident(LoginRequiredMixin,View):
    def get(self,request):
        id1 = request.GET.get('id',None)
        isIncident1 = request.GET.get('isincident',None)
        analyse_by1 = request.user.id
        

        obj = Event_alert.objects.get(id=id1)
        obj.is_incident = isIncident1
        obj.analyse_by_id = analyse_by1
        obj.analyse_at = datetime.now()+timedelta(hours=7)
        obj.save()

        event = {'id':obj.id}

        data = {
            'event': event
        }
        return JsonResponse(data)

class Closed_Event(LoginRequiredMixin,View):
    def get(self,request):
        id1 = request.GET.get('id',None)
        isClosed1 = request.GET.get('isclosed',None)
        closed_by1 = request.user.id
        

        obj = Event_alert.objects.get(id=id1)
        obj.is_closed = isClosed1
        obj.closed_by_id = closed_by1
        obj.closed_at = datetime.now()+timedelta(hours=7)
        obj.save()

        event = {'id':obj.id}

        data = {
            'event': event
        }
        return JsonResponse(data)

class Update_Memo(LoginRequiredMixin,View):
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



class Event_getRuleViewAPI(viewsets.ModelViewSet):            
    queryset = Event_rule.objects.all()
    
    serializer_class = Event_ruleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['rule']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)