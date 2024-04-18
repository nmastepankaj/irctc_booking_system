from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from utils.encrypt import encrypt_message
from account.models import AdminSecret

class AdminAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-IRCTC-API-KEY-SECRET')
        if not api_key:
            raise AuthenticationFailed('No api key provided')
        

        try:
            user = AdminSecret.objects.get(api_key=api_key).user
        except:
            raise AuthenticationFailed('Authentication failed')

        return (user, None)