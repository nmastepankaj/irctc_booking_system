from django.urls import path
from booking.views.admin import AdminBookingViewSet

urlpatterns = [
    path("add_train",AdminBookingViewSet.as_view({"post":"add_train"})),
    path("add_train_schedule",AdminBookingViewSet.as_view({"post":"add_train_schedule"})),
    path("update_train_schedule/<int:schedule_id>",AdminBookingViewSet.as_view({"patch":"update_train_schedule"})),
]