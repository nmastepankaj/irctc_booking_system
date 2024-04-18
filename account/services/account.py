from account.models import Account
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Optional, Tuple
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

class AccountService:
    
    @classmethod
    def user_authentication(cls,email,password):
        """Verify User Details"""

        user = authenticate(email=email, password=password)
        return user
    

    @classmethod
    def get_tokens_for_user(cls, user) -> dict:
        """Get tokens for the given user"""

        refresh = RefreshToken.for_user(user)
        refresh['email'] = user.email
        refresh['user_id'] = user.id
        refresh['name'] = user.name

        access_token = refresh.access_token
        
        return {
            'refresh': str(refresh),
            'access': str(access_token),
        }
    
    

    @classmethod
    @transaction.atomic()
    def create_user(cls, name, email, password) -> Tuple[Optional[Account],Optional[str]]:
        """Create a new user with the provided name, mobile_number, and password"""

        if Account.objects.filter(email=email).exists():
            logger.warning(f"User with {email} already registered")
            return None, "User already exists"
        else:
            user = Account(name=name, email=email)
            user.is_active = True
            user.set_password(password)
            user.save()            
            return user, "User registered successfully!"
     

    @classmethod
    def verify_user(cls, email, password) -> Optional[dict]:
        """Verify user and return the token if user is active and authenticated successfully"""
        user = cls.user_authentication(email,password)

        
        if user is None:
            logger.warning(f"email or password didn't match {email}")
            return None
       
        if user.is_active:
            token = cls.get_tokens_for_user(user)
            return token
        else:
            logger.warning(f"User {user.name} and {user.email} is not active")
            return None
           