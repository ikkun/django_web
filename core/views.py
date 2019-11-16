from django.http import JsonResponse
from django.shortcuts import render

def test_view(request):
    data ={
        'name':'ikkun',
        'age':37
    }
    return JsonResponse(data)
