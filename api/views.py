from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.views import APIView
from student.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class UserSerializerView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)

class CreateUserSerializerView(APIView):    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
class UpdateUserSerializerView(APIView):
    def put(self, request, id):
       
        user =get_object_or_404(User, id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, data=serializer.data)
        
class DeleteUserSerializerView(APIView):
    def delete(self, request, id):
        instance = get_object_or_404(User, id=id)
        serializer = UserSerializer(instance)
        serializer.delete(instance)
        return Response(data=serializer.data)

class UserDetailApiView(APIView):
     def get(self, request, id):
        user =get_object_or_404(User,id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
