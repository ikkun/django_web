from django.shortcuts import render
from django.http import HttpResponse
from .models import Programming_Authors,ProgrammingFramework
import csv

# Create your views here.
def authors(request):
    # return HttpResponse("Hello my first app")
    return render(request=request,
                  template_name="programming/home.html",
                  context={"programming_authors":Programming_Authors.objects.all}
                  )

def framework(request):
    framework_obj = ProgrammingFramework.objects.all
    return render(request,
                'programming/framework.html',
                {'frame_obj':framework_obj}
                )
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="Framework.csv"'

    writer = csv.writer(response)
    writer.writerow(['Framework','Framework Types','Programming Languages'])

    frameworks = ProgrammingFramework.objects.all().values_list('framework_name',
                                                            'framework_type',
                                                            'programming_authors')
    for myFramework in frameworks:
        writer.writerow(myFramework)
    
    return response
