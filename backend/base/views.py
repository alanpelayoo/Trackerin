from django.shortcuts import render
from .models import Project
from .serializer import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all() #Query set
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    project  = Project.objects.get(_id = pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
