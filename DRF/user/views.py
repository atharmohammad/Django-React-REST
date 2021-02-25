from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class CustomUserCreate(APIView):
    permission_classes = [AllowAny] #permission_classes to define how authentication takes place

    def post(self,request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        #using serializers, serializers used for taking data in certain standard according to you models
        if reg_serializer.is_valid():
            newuser = reg_serializer.save() #new user has been created
            if newuser:
                return Response(status=status.HTTP_201_CREATED)

        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BlackListTokenView(APIView):
    permission_classes = [AllowAny]
    # authentication_classes = ()
    
    def post(self,request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)
