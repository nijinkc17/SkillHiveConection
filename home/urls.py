from django.urls import path
from .views import *

urlpatterns = [
    path('home',HomeView.as_view(),name="home"),
    path('homeContent/',HomeContentView.as_view(),name="homeContent"),
    path('homeContent/service/<int:id>',ServiceListView.as_view(),name="serviceList"),



    
] 