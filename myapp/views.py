from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    name_temp= "Dhruv"
    # used to send dynamic data
    return render(request,'index.html',{'name':name_temp})
