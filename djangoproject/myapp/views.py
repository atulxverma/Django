from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    return render(request, "index.html", {"jobs": jobs})

def about(request):
    return HttpResponse("about page")