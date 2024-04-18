from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from account.custom_permission import IsAdmin
from account.custom_authentication_classes import AdminAuthentication

class PublicViewSet(viewsets.ViewSet):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    permission_classes = []

class UserViewSet(viewsets.ViewSet):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class AdminViewSet(viewsets.ViewSet):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [AdminAuthentication]