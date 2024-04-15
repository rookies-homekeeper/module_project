from django.shortcuts import render,get_object_or_404,redirect
from .models import Stuff
from .forms import StuffForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime,timedelta
from .forms import StuffUpdateForm

# Create your views here.

def index(request):
    stuffs=Stuff.objects.all()
    context={'stuffs':stuffs}
    return render(request,'mall/index.html',context)

def detail(request,stuff_id):
    stuff = get_object_or_404(Stuff, pk=stuff_id)
    context = {'stuff': stuff, 'user': request.user}
    return render(request, 'mall/detail.html', context)

@login_required  # 로그인 필요
def register(request):
    if request.method == "POST":
        form = StuffForm(request.POST, request.FILES)
        if form.is_valid():
            stuff = form.save(commit=False)
            stuff.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            stuff.save()
            return redirect('mall:index')
    else:
        form = StuffForm()
    return render(request, 'mall/register.html', {'form': form})

@login_required(login_url='common:login')

def info(request):
    return render(request,'mall/info.html',context)

def logout_view(request):
    logout(request)
    return redirect('mall/')

@login_required
def toggle_like(request, stuff_id):
    stuff = get_object_or_404(Stuff, id=stuff_id)
    if request.user in stuff.liked_by.all():
        stuff.liked_by.remove(request.user)
    else:
        stuff.liked_by.add(request.user)
    return redirect('mall:detail', stuff_id=stuff_id)  ########


@login_required
def my_likes(request):
    my_liked_stuffs = request.user.liked_stuffs.all()
    return render(request, 'mall/my_likes.html', {'my_liked_stuffs': my_liked_stuffs}) #######
    
def delete_stuff(request, stuff_id):
    stuff = Stuff.objects.get(pk=stuff_id)
    stuff.delete_stuff()
    return redirect('mall:index')

def update_stuff(request, stuff_id):
    stuff = get_object_or_404(Stuff, pk=stuff_id)
    if request.method == 'POST':
        form = StuffForm(request.POST, request.FILES, instance=stuff)
        if form.is_valid():
            form.save()
            return redirect('mall:detail', stuff_id=stuff_id)
    else:
        form = StuffForm(instance=stuff)
    return render(request, 'mall/update_stuff.html', {'form': form})

def search_results(request):
    query = request.GET.get('q', '')
    if query:
        search_results = Stuff.objects.filter(name__icontains=query)
    else:
        search_results = Stuff.objects.none()
    
    return render(request, 'mall/search_results.html', {
        'query': query,
        'search_results': search_results
    })

def search_view(request):
    query = request.GET.get('q', '')
    context = {'search_results': search_results}
    return render(request, 'search_results.html', context)