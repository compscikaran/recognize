from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Scan
from .tessfuncs import getImage,imageText
import os
# Create your views here.
def home(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def scan(request):
    if request.method == 'POST':
        if request.POST['name'] and request.FILES['image']:
            scan = Scan()
            scan.name = request.POST['name']
            scan.image = request.FILES['image']
            scan.datestamp = timezone.datetime.now()
            scan.save()
            image = getImage(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + scan.image.url)
            text = imageText(image)
            return redirect('editor',{'ret':text})
        else:
            return render(request,'scan.html',{'error': 'All fields are required'})    
    else:
        return render(request,'scan.html')

def editor(request):
    return render(request,'editor.html',{'text':text})

