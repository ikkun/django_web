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

def ips_map(request):
    context={"title":"IPS Attack World Map"}
    fullpath="{}/data_analytics/threat_ips.csv".format(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(fullpath)
    df_country_attack=df[['sourceGeoLocation','alertCount']].groupby(['sourceGeoLocation'])['alertCount'].sum().reset_index().sort_values(by='alertCount',ascending=False)
    if not df_country_attack.empty:
        df_country_attack['sourceGeoLocation']=df_country_attack['sourceGeoLocation'].str.lower()
        country_attack_dict=[]
        for index,row in df_country_attack.iterrows():
            country_attack_dict.append([row['sourceGeoLocation'],row['alertCount']])
        print(country_attack_dict)
        context['ips_map']=country_attack_dict
    # data = df_country_attack.to_json(index=True,orient='records')
    # print(data)
    
    return render(request, 'ips/ips_map.html', context=context)