from django.shortcuts import render
from homepage_app.models import Destination


# Create your views here.
# 1.def index(request):
#     return render(request,'homepage/index.html',{'price':700})

def index(request):
    dests=Destination.objects.all()
    return render(request,'homepage/index.html',{'dests':dests})