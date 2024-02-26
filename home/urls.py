from django.urls import path
from .views import *

urlpatterns = [
    path('home',HomeView.as_view(),name="home"),
    path('profile',ProfileView.as_view(),name='profile'),
    path('homeContent/',HomeContentView.as_view(),name="homeContent"),
    path('homeContent/service/<int:id>',ServiceListView.as_view(),name="serviceList"),
    path('service/details/<int:id>',ServiceDetailsView.as_view(),name='serviceDetail'),
    path('checkout/<int:id>/',CheckOutView.as_view(),name='checkout'),


    path('booking/page/<int:id>',BookingPageView.as_view(),name='bookingPage'),
    path('cartlist/',BookingHistoryView.as_view(),name="bookHistory"),





    
] 