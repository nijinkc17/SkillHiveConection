from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Service,OurServices,BookingPage,Booking
from django.views.generic import View
from django.contrib import messages


# Create your views here.


class HomeView(TemplateView):
    # template_name='test_layout.html'
    template_name='hm.html'

class ProfileView(View):
    def get(self,request):
        return render(request,'profile.html')




    

# class HomeContentView(TemplateView):
    # template_name='test_layout.html'
    # template_name='hm_content.html'
    

    
class HomeContentView(ListView):
    template_name="hm_content.html"
    queryset=Service.objects.all()
    context_object_name="data"


class ServiceListView(ListView):
    template_name="serviceList.html"
    queryset=OurServices.objects.all()
    context_object_name="data"

    def get_queryset(self) -> QuerySet[Any]:
        service=Service.objects.get(id=self.kwargs['id'])
        return OurServices.objects.filter(our_service=service)  
    

class ServiceDetailsView(DetailView):
    template_name="service_det.html"
    pk_url_kwarg='id'
    queryset=OurServices.objects.all()
    context_object_name="data"
    

# class BookingPageView(View):
#     def get(self,request,**kwargs):
#         sid=kwargs.get('id')
#         ourservice=OurServices.objects.get(id=sid)
#         user=request.user
#         BookingPage.objects.create(ourservices=ourservice,user=user)
#         messages.success(request,"redirected to booking!!")
#         return redirect('home')
    
# class CheckOutView(View):
#     def get(self,request,**kwargs):
#         return render(request,'checkout.html')
#     def post(self,request,**kwargs):
#         cid=kwargs.get('id')
#         book=BookingPage.objects.get(id=cid)
#         ph=request.POST.get('phone')
#         add=request.POST.get('address')
#         Booking.objects.create(booking=book,phone=ph,address=add)
#         book.status='pending'
#         book.save()
#         messages.success(request,'Booking confirmed..!')
#         return redirect('home')
    


from django.http import Http404


class BookingPageView(View):
    def get(self, request, **kwargs):
        sid = kwargs.get('id')
        try:
            our_service = OurServices.objects.get(id=sid)
            user = request.user
            BookingPage.objects.create(ourservices=our_service, user=user)
            messages.success(request, "Redirected to booking!!")
            return redirect('home')
        except OurServices.DoesNotExist:
            raise Http404("OurServices does not exist")
        

class BookingHistoryView(ListView):
    template_name='history.html'
    queryset=BookingPage.objects.all()
    context_object_name="book"

    def get_queryset(self):
        return BookingPage.objects.filter(user=self.request.user,status='pending')
        


class CheckOutView(View):
    def get(self, request, **kwargs):
        return render(request, 'checkout.html')

    def post(self, request, **kwargs):
        cid = kwargs.get('id')
        try:
            booking_page = BookingPage.objects.get(id=cid)
        except BookingPage.DoesNotExist:
            raise Http404("BookingPage does not exist")

        ph = request.POST.get('phone')
        add = request.POST.get('address')
        Booking.objects.create(booking=booking_page, phone=ph, address=add)
        booking_page.status = 'pending'
        booking_page.save()
        messages.success(request, 'Booking confirmed..!')
        return redirect('home')
