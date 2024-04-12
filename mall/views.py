from django.shortcuts import render,get_object_or_404,redirect
from .models import Stuff,Order
from .forms import StuffForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime,timedelta
# Create your views here.

def index(request):
    stuffs=Stuff.objects.all()
    context={'stuffs':stuffs}
    return render(request,'mall/index.html',context)

def detail(request,stuff_id):
    stuff=Stuff.objects.get(id=stuff_id)
    context={'stuff':stuff}
    return render(request,'mall/detail.html',context)

def register(request):
    if request.method=="POST":
        stuff=Stuff(name=request.POST.get('name'),price=request.POST.get('price'),detail=request.POST.get('detail'),image=request.FILES.get('image'))
        stuff.pub_date=timezone.now()+timedelta(hours=9)
        stuff.save()
        return redirect('mall:index')
    else:
        form=StuffForm()
        return render(request,'mall/register.html',{'form':form})

@login_required(login_url='common:login')
def info(request):
    return render(request,'mall/info.html',context)