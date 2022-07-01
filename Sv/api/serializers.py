from dataclasses import field
from pyexpat import model
from unittest import mock
from rest_framework import serializers
from base.models import doctor, registererForm, customer

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields ='__all__'
class RegisteredFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = registererForm
        fields ='__all__'        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields ='__all__'             