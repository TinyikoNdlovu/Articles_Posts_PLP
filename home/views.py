from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>Our Home Page</h1>")

# create view -> url conf/mapping -> Template
#
# Model
