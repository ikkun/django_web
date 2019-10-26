from django.shortcuts import render
from django.http import HttpResponse
from .models import Programming_Authors,ProgrammingFramework

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
