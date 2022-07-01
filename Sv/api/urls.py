from django.urls import path
from . import views

urlpatterns = [
    
    path('getDoctor/',views.getData),
    path('updateDoctor/',views.updateDoctor),
    path('getRegistered/',views.getRegisteredForm),
    path('getCustomer/',views.getCustomer),
    path('getDoctorByName/',views.getDoctor),
    path('addDoctor/',views.adddoctor),
    path('addCustomer/',views.addCustomer),
    path('addschedule/',views.addRegisteredForm)

]
