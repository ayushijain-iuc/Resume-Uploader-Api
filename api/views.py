from django.shortcuts import render
from rest_framework import status
from .  serializer import *
from . models import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


class ProfileView(APIView):
    def post(self,request,format=None):
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resume uploaded successfully','status':'success','candidate':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self,request,format=None):
        candidates=Profile.objects.all()
        serializer=ProfileSerializer(candidates,many=True)
        return Response({'status':'success','candidate':serializer.data},status=status.HTTP_200_OK)
    

# Create your views here.
