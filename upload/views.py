from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Scan,BlockModel
from .tessfuncs import getImage,imageText
import os
from .chain import last_block,verify_block_exists,verify_chain
from django.contrib.auth import login, authenticate
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
            scan.language = request.POST['language']
            scan.doctype = request.POST['type']
            scan.save()
            image = getImage(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + scan.image.url)
            text = imageText(image,scan.language)
            scan.text = text
            scan.save()
            block = BlockModel()
            block.text = text
            block.previous_hash = last_block().block_hash
            block.block_hash = block.hash_block()
            block.save()
            link = scan.image.url

            return render(request,'editor.html',{'data': text.replace("\n","<br>"),'link': link})
        else:
            return render(request,'scan.html',{'error': 'All fields are required'})    
    else:
        return render(request,'scan.html')

def verify(request):
    if request.method == 'POST':
        scan = Scan()
        scan.name = request.POST['name']
        scan.image = request.FILES['image']
        scan.datestamp = timezone.datetime.now()
        scan.language = request.POST['language']
        scan.save()
        image = getImage(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + scan.image.url)
        text = imageText(image,scan.language)
        for blocki in BlockModel.objects.all():
            bl = BlockModel(0,text,blocki.previous_hash)
            bl.block_hash = bl.hash_block()
            for blockj in BlockModel.objects.all():
                if blockj.block_hash == bl.block_hash:
                    if verify_chain():
                        return render(request,'result.html',{'val':'Document Verified'})
        return render(request,'result.html',{'val':'Document Not Verified'})
    else:
        return render(request,'verify.html',{'error': 'All fields are required'})       
