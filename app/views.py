from django.shortcuts import render,HttpResponseRedirect
from .forms import LoginForm,TractorForm
from .models import TractorDetail
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import MyUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    fm=TractorDetail.objects.all()
    return render(request,'app/tractorlist.html',{'form':fm})

def detail_page(request,pk):
    dt=TractorDetail.objects.filter(pk=pk)
    return render(request,'app/detail.html',{'data':dt})

def registration_page(request):
    if request.method=="POST":
        fm=MyUserCreationForm(request.POST)
        if fm.is_valid() :
            messages.success(request,'Congratulations You have registered  ')
            fm.save()
        fm=MyUserCreationForm()
    else:       
        fm=MyUserCreationForm()
    return render(request,'app/registration.html',{'form':fm})

def login_page(request):
    if request.method=="POST":
        fm=LoginForm(request,data=request.POST)
        if fm.is_valid():
            un=fm.cleaned_data['username']
            pa=fm.cleaned_data['password']
            User=authenticate(username=un,password=pa)
            if User is not None:
                login(request,User)
                return HttpResponseRedirect('/tractorreg/')
    else:
        fm=LoginForm()
    return render(request,'app/login.html',{'form':fm})
    
@ login_required(login_url='/login/') 
def tractorreg_page(request):
     if request.method=="POST":
          user=request.user
          fms=TractorForm(request.POST)
          if fms.is_valid():
               brand= fms.cleaned_data['brand']
               model_no= fms.cleaned_data['model_no']
               hp_category= fms.cleaned_data['hp_category']
               implements= fms.cleaned_data['implements']
               fm=TractorDetail(user=user,brand=brand,model_no=model_no,hp_category=hp_category,implements=implements)
               fm.save()
               messages.success(request,'Congratulations detail Updated Succefully ')
               fm=TractorForm()
     else:
          fm=TractorForm()
     return render(request,'app/tractorreg.html',{'form':fm,'active':'btn-primary'})
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')

    