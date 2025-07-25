from django.shortcuts import render,HttpResponse

# Create your views here.
def hrhome(request):

    return render(request,"HRtemp/hrhome.html")



