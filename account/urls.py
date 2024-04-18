from django.urls import path
from account.views import AccountViewSet

urlpatterns = [
    path("login",AccountViewSet.as_view({"post":"login"})),
    path("register",AccountViewSet.as_view({"post":"create_account"})),
]