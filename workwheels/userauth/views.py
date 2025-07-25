from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse

# Create your views here.
def authhome(request):

    return render(request,"mastertemp.html")


def login(request):
    
    return render(request,"mastertemp.html")