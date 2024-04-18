from rest_framework import serializers

class BookSeatSerializer(serializers.Serializer):
    train_number = serializers.IntegerField()
    schedule_id = serializers.IntegerField()
    number_of_seats = serializers.IntegerField()


class BookingResponseSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    number_of_seats = serializers.IntegerField()
    total_price = serializers.FloatField()
    booking_date = serializers.DateTimeField()
    booking_status = serializers.BooleanField()
    schedule_id = serializers.IntegerField()
    payment_status = serializers.BooleanField()

class TrainSerializer(serializers.Serializer):
    source = serializers.CharField(max_length=100)
    destination = serializers.CharField(max_length=100)
    train_number = serializers.CharField(max_length=100)
    train_name = serializers.CharField(max_length=100)
    total_seats = serializers.IntegerField()
    price = serializers.FloatField()

class TrainScheduleSerializer(serializers.Serializer):
    train = TrainSerializer()
    journey_date = serializers.DateField()
    departure_time = serializers.TimeField()
    arrival_time = serializers.TimeField()
    journey_end_date = serializers.DateField()
    journey_end_time = serializers.TimeField()
    available_seats = serializers.IntegerField()

class AddTrainScheduleSerializer(serializers.Serializer):
    train_number = serializers.IntegerField()
    journey_date = serializers.DateField()
    departure_time = serializers.TimeField()
    arrival_time = serializers.TimeField()
    journey_end_date = serializers.DateField()
    journey_end_time = serializers.TimeField()
    available_seats = serializers.IntegerField()

class UpdateTrainScheduleSerializer(serializers.Serializer):
    journey_date = serializers.DateField(required=False)
    departure_time = serializers.TimeField(required=False)
    arrival_time = serializers.TimeField(required=False)
    journey_end_date = serializers.DateField(required=False)
    journey_end_time = serializers.TimeField(required=False)
    available_seats = serializers.IntegerField(required=False)


class TrainScheduleRequestSerializer(serializers.Serializer):
    source = serializers.CharField(max_length=100)
    destination = serializers.CharField(max_length=100)
    journey_date = serializers.DateField()

class SeatSerializer(serializers.Serializer):
    seat_number = serializers.IntegerField()

class FullBookingDetailsSerializer(serializers.Serializer):
    train = TrainSerializer()
    schedule = TrainScheduleSerializer()
    number_of_seats = serializers.IntegerField()
    total_price = serializers.FloatField()
    booking_date = serializers.DateTimeField()
    booking_status = serializers.BooleanField()