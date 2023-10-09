from django.shortcuts import render
from .models import * 
from .serailizers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
# Create your views here.

class Task1ListView(APIView):
    def get(self,request):
        task = Task1.objects.all()
        serializer = Task1Serailizer(task,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializers = Task1Serailizer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        

class Task1CRUD(APIView):
    def get(self,request,pk):
        try:
            task = Task1.objects.get(pk=pk)
        except task.DoesnotExit:
            return Response({'task does not exits'},status= status.HTTP_404_NOTFOUND)
        serailizer = Task1Serailizer(task)
        return Response(serailizer.data)
    
    def put(self,request,pk):
        task = Task1.objects.get(pk=pk)
        serializer = Task1Serailizer(task,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self,request,pk):
        task = Task1.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

            
@api_view(['GET','POST'])
def TaskCompletionList(request):
    if request.method == 'GET':
        task_completion_status = TaskCompletionstatus.objects.all()
        serializer = TaskCompletionstatusSerializer(task_completion_status, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskCompletionstatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
@api_view(['GET','PUT','DELETE'])
def TaskCompletionView(request,pk):
    if request.method == 'GET':
        try:
            taskcomplete  = TaskCompletionstatus.objects.get(pk=pk)
        except TaskCompletionstatus.DoesNotExist:
            return Response({'error':'task not found'},status=status.HTTP_404_NOTFOUND)
        serializer = TaskCompletionstatusSerializer(taskcomplete)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        taskcomplete = TaskCompletionstatus.objects.get(pk=pk)
        serializer = TaskCompletionstatusSerializer(taskcomplete,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        taskcomplete = TaskCompletionstatus.objects.get(pk=pk)
        taskcomplete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
                
class TaskCreatorDetailView(generics.RetrieveAPIView):
    queryset = TaskCreator.objects.all()
    serializer_class = TaskCreatorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        created_tasks = instance.created_tasks.all()
        serialized_data = {
            'user': TaskCreatorSerializer(user).data,
            'created_tasks': TaskCreatorSerializer(created_tasks, many=True).data
        }
        return Response(serialized_data)