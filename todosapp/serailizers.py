from rest_framework import serializers
from todosapp.models import * 

class Task1Serailizer(serializers.ModelSerializer):
    class Meta:
        model = Task1 
        fields = '__all__'
        
class TaskCompletionstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCompletionstatus
        fields = '__all__'
        
class TaskCreatorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    created_tasks = Task1Serailizer(many=True, read_only=True)
    class Meta:
        model = TaskCreator
        fields = '__all__'
        
class UserSignUpSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField()


class UserSignInSerializer(serializers.Serializer):
    
    email = serializers.CharField()
    password = serializers.CharField()
    
class ForgotpasswordSerializer(serializers.Serializer):
    email = serializers.CharField()
    
class ForgetPasswordVerifySerializer(serializers.Serializer):
    email = serializers.CharField()
    new_password = serializers.CharField()
    otp = serializers.IntegerField()
    