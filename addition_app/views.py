from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html', {'name': 'venkey'})

def add(request):
    value1=request.POST.get('num1')
    value2=request.POST.get('num2')
    res=int(value1)+int(value2)
    return render(request,'result.html',{'result':res})