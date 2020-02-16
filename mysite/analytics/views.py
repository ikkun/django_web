from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core import serializers

def ips_with_pivot(request):
    print(os.path.dirname(os.path.abspath(__file__)))
    return render(request, 'ips/ips_with_pivot.html', {})

def ips_pivot_data(request):
    # csvfile = request.FILES["dashboard_order.csv"]
    fullpath="{}/data_analytics/threat_ips.csv".format(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(fullpath)
    data = df.to_json(index=True,orient='records')
   
    # print(data)
    # fullpath="{}/dashboard_order.csv".format(os.path.dirname(os.path.abspath(__file__)))
    # df = pd.read_csv(fullpath)
    # data = df.to_json(index=True,orient='records')
   
    # print(data)
    # print(dataset)
    
    # # dataset = {'test':'test'}
    # data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

# Create your views here.
