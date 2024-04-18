from account.custom_viewset import PrivateViewSet, PublicViewSet
from account.serializers import AccountSerializer, LoginSerializer
from account.services.account import AccountService

from rest_framework.response import Response
from rest_framework import status
from utils.response import error_response, success_response

# Create your views here.
class AccountViewSet(PublicViewSet):
    
    def create_account(self, request):
        """Register user view"""
        serializer = AccountSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(data=serializer.errors,msg="", status=status.HTTP_400_BAD_REQUEST)
        
        user, message = AccountService.create_user(**serializer.validated_data)
        
        if not user:
            return error_response(msg=message,data={}, status=status.HTTP_400_BAD_REQUEST)
        
        return success_response(status=status.HTTP_201_CREATED,msg= message,data= {})

    def login(self, request):
        """Login user view"""
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(data=serializer.errors,msg="", status=status.HTTP_400_BAD_REQUEST)
        
        response = AccountService.verify_user(**serializer.validated_data)
        
        if not response:
            return error_response(msg="Invalid credentials",data={}, status=status.HTTP_400_BAD_REQUEST)
        
        return success_response(status=status.HTTP_200_OK,msg= "User logged in successfully",data= response)

