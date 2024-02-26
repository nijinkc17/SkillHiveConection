from django.urls import path
from .views import *

urlpatterns = [
    path('reg',RegView.as_view(),name="signup"),
    path('logout',LgOutView.as_view(),name='logout')




    
] 
