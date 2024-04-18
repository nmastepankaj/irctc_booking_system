from django.db import models
from account.models import BaseModel, Account

class Train(BaseModel):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    train_number = models.CharField(max_length=100)
    train_name = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.train_name

class TrainSchedule(BaseModel):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    journey_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    journey_end_date = models.DateField()
    journey_end_time = models.TimeField()

    available_seats = models.IntegerField()

    def __str__(self):
        return self.train.train_name

class Booking(BaseModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    total_price = models.FloatField()
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_status = models.BooleanField(default=False)
    schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

class Seat(BaseModel):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    status = models.BooleanField(default=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    journey_date = models.DateField()

    def __str__(self):
        return self.train.train_name + ' ' + str(self.seat_number) + ' ' + str(self.booking.user.email) + ' ' + str(self.journey_date)
