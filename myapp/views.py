from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    context={
        "Name":"Dhruv",
        "Address":"41, Hamlyn Rd., St John's NL, Canada",
        "Gender":"Male",
        "Likes":"..................."
    }
    # used to send dynamic data
    return render(request,'index.html',context)
