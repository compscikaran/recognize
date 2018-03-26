from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    date = datetime.datetime.now()
    return render(request,'base.html',{'date':date})

def about(request):
    return render(request,'login.html')