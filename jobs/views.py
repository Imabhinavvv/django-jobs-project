from django.shortcuts import render
from .models import Job
# Create your views here.

def home(request):
    job_list=Job.objects.all()
    print(job_list)
    context={'job_list':job_list}
    return render(request,'home.html',context)
    
    