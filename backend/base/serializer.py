#Wrap our model and return json

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProjectSerializer(serializers.ModelSerializer): #Wrap our model and turns it into JSon
    class Meta:
        model = Project
        fields = '__all__'