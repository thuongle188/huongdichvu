from email.policy import default
from turtle import update
from unicodedata import name
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import customer
from base.models import doctor, registererForm
from .serializers import DoctorSerializer, RegisteredFormSerializer, CustomerSerializer

@api_view(['GET'])
def getData(request):
   doctors = doctor.objects.all()
   ser = DoctorSerializer(doctors, many = True)
   return Response(ser.data)
@api_view(['GET'])
def getDoctor(request):
   names = doctor.name
   doctors = doctor.objects.filter(names)
   ser = DoctorSerializer(doctors, many = True)
   return Response(ser.data)  
@api_view(['PUT'])
def updateDoctor(request):
   doctors = doctor.objects.filter(id = request.data).update(time = 'No')
   ser = DoctorSerializer(doctors, many = True)
   if ser.is_valid():
       ser.update()
   return Response(ser.data)
@api_view(['POST'])
def adddoctor(request):
   ser = DoctorSerializer(data=request.data)
   if ser.is_valid():
       ser.save()
   return Response(ser.data)

@api_view(['POST'])
def addRegisteredForm(request):
   ser = RegisteredFormSerializer(data=request.data)
   if ser.is_valid():
      ser.save()
   return Response(ser.data)
@api_view(['GET'])
def getRegisteredForm(request):
   forms = registererForm.objects.filter(phone = request.data)
   ser = RegisteredFormSerializer(forms, many = True)
   return Response(ser.data)    

@api_view(['GET'])
def getCustomer(request):
   customers = customer.objects.all()
   ser = CustomerSerializer(customers, many = True)
   return Response(ser.data)
@api_view(['POST'])
def addCustomer(request):
   ser = CustomerSerializer(data=request.data)
   if ser.is_valid():
       ser.save()
   return Response(ser.data)