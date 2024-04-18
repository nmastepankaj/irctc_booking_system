from django.contrib import admin
from booking.models import Booking, Seat, Train, TrainSchedule

# Register your models here.
admin.site.register(Train)
admin.site.register(TrainSchedule)
admin.site.register(Booking)
admin.site.register(Seat)
