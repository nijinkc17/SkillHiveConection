from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from django.urls import reverse, reverse_lazy
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse




class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('log')
    def form_valid(self, form):
        messages.success(self.request,"Registration successful !!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"Validation failed")
        return super().form_invalid(form)



class LogView(FormView):
    template_name='log.html'
    form_class=LogForm
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get("user_name")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                if user.is_superuser:
                    return redirect(reverse("admin:index"))
                else:
                    messages.success(request,"login successfull !!")
                    return redirect('home')
                # return HttpResponse('login done')
            else:
                messages.success(request,"Invalid username or password !!")
                return redirect('log')
        return render(request,"log.html",{"form":form_data})
    

