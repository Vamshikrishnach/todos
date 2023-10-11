from django.shortcuts import render
from .models import * 
from .serailizers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics,viewsets,mixins
from rest_framework.authtoken.models import Token
from todosproject.users.models import generate_token
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
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
    
class UserSiginUpViewset(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = UserSignUpSerializer
    permission_classes = [AllowAny,]
    
    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop('password')
        email = serializer.validated_data.get('email',None)
        
        if get_user_model().objects.filter(email=email).exists():
            return Response({'Error':'User this email already exits'},status=status.HTTP_400_BAD_REQUEST)
        
        user = get_user_model().objects.create_user(
            username = serializer.validated_data['email'],
            email = serializer.validated_data['email'],
            password = password,
            name = serializer.validated_data['name']
        )

       # Set user role and generate token
        user_role = Group.objects.get(name="admin")
        user.groups.add(user_role)
        user.save()
        generate_token(user)
        return Response("User Created Successfully", status=status.HTTP_201_CREATED)


class UserSignInViewset(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = UserSignInSerializer
    permission_classes = [AllowAny,]
    
    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        User = get_user_model()
        
        if User.objects.filter(email=email):
            user = User.objects.get(email=email)
            token = Token.objects.get(user=user)
            if user.check_password(password):
                groups = [group.name for group in  user.groups.all()]
                return Response({'Response':'user logged in sucessfully',
                                 'token' : token.key,
                                 'id' : user.id,
                                 'first_name':user.name,
                                 'email':user.email,
                                 'groups':groups,
                                })
            else:
                return Response({'Error':'Incorrect Password'},status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Email does not exists"}, status=status.HTTP_400_BAD_REQUEST)

def generate_otp():
    import random
    import math
    digits = [i for i in range(0, 10)]
    random_str = ''
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    return random_str
    
class ForgetPasswordViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = generate_otp()
        if get_user_model().objects.filter(email=email).exists():

            user = get_user_model().objects.get(email=email)
            user.otp = '1234'
            user.save()
            return Response({"Response": "OTP sent to your email"})
        else:
            return Response({"Error": "email does not exists"},  status=status.HTTP_400_BAD_REQUEST)


class ForgetPasswordVerifyViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ForgetPasswordVerifySerializer
    permission_classes = [AllowAny,]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']

        if get_user_model().objects.filter(email=email).exists():
            user = get_user_model().objects.get(email=email)
            if user.otp == str(otp):
                user.password = make_password(new_password)
                user.save()
                return Response({"Response": "password updated successfully"})
            else:
                return Response({"Response": "Otp did not match"},  status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "email does not exists"},  status=status.HTTP_400_BAD_REQUEST)
        