from django.shortcuts import render
from django.http import HttpResponse

jobs = [
  { "title": "Frontend Developer", "company": "Google", "location": "Remote", "salary": "$120k" },
  { "title": "Product Designer", "company": "Figma", "location": "San Francisco, CA", "salary": "$135k" },
  { "title": "Backend Engineer", "company": "Stripe", "location": "New York, NY", "salary": "$145k" },
  { "title": "Data Analyst", "company": "Netflix", "location": "Remote", "salary": "$110k" },
  { "title": "DevOps Engineer", "company": "Amazon", "location": "Seattle, WA", "salary": "$150k" },
  { "title": "Marketing Manager", "company": "Airbnb", "location": "Remote", "salary": "$98k" },
];

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("about page")