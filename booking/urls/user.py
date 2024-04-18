from django.urls import path
from booking.views.user import BookingViewSet

urlpatterns = [
    path("book_ticket",BookingViewSet.as_view({"post":"create_booking"})),
    path("get_trains",BookingViewSet.as_view({"get":"get_trains"})),
    path("get_booking/<str:booking_uuid>",BookingViewSet.as_view({"get":"get_booking"})),
    
]