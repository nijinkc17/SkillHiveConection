from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Service,OurServices

# Create your views here.


class HomeView(TemplateView):
    # template_name='test_layout.html'
    template_name='hm.html'




    

# class HomeContentView(TemplateView):
    # template_name='test_layout.html'
    # template_name='hm_content.html'
    

    
class HomeContentView(ListView):
    template_name="hm_content.html"
    queryset=Service.objects.all()
    context_object_name="data"


    # def get_context_data(self, **kwargs):
    #     form=ReviewForm()
    #     context=super().get_context_data(**kwargs)
    #     context['form']=form
    #     pro=kwargs.get('object')
    #     reviews=Review.objects.filter(product=pro)
    #     context['review']=reviews
    #     return context

class ServiceListView(ListView):
    template_name="serviceList.html"
    queryset=OurServices.objects.all()
    context_object_name="data"

    def get_queryset(self) -> QuerySet[Any]:
        service=Service.objects.get(id=self.kwargs['id'])
        return OurServices.objects.filter(our_service=service)  
