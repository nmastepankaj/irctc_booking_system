from typing import Optional, Tuple, Dict
from booking.models import Train, TrainSchedule, Booking, Seat
from account.models import Account
from django.utils import timezone
from booking.serializers import BookingResponseSerializer, TrainScheduleSerializer, SeatSerializer, FullBookingDetailsSerializer, TrainSerializer
from django.db import transaction

class BookingService:

    @classmethod
    @transaction.atomic
    def create_booking(cls, user: Account, data: Dict[str, str]) -> Tuple[Optional[Dict], str]:
        train_number = data['train_number']
        schedule_id = data['schedule_id']
        number_of_seats = data['number_of_seats']

        train = Train.objects.filter(train_number=train_number).first()
        if not train:
            return None, "Train not found"
        
        schedule = TrainSchedule.objects.filter(id=schedule_id).first()

        # import pdb; pdb.set_trace()
        if not schedule:
            return None, "Schedule not found"

        if number_of_seats > schedule.available_seats:
            return None, "Seats not available"

        total_price = number_of_seats * train.price
        schedule = TrainSchedule.objects.select_for_update().get(id=schedule.id)

        booking = Booking.objects.create(
            user=user,
            train=train,
            number_of_seats=number_of_seats,
            total_price=total_price,
            schedule=schedule,
            payment_status=True,
            booking_status=True,
            booking_date=timezone.now()
        )

        seats = []
        # bulk create seat
        for i in range(number_of_seats):
            seat = Seat(
                train=train,
                seat_number=schedule.available_seats - i,
                status=True,
                booking=booking,
                journey_date=schedule.journey_date
            )
            seats.append(seat)

        Seat.objects.bulk_create(seats)



        if schedule.available_seats >= number_of_seats:
            schedule.available_seats -= number_of_seats
            schedule.save()
        else:
            return None, "Seats not available"

        return BookingResponseSerializer(booking).data, "Booking created successfully!"
    

    @classmethod
    def get_trains(cls, data: Dict[str, str]) -> Optional[Dict]:
        source = data['source']
        destination = data['destination']
        journey_date = data['journey_date']

        trains = TrainSchedule.objects.filter(journey_date=journey_date, train__source=source, train__destination=destination).distinct()
        if not trains:
            return None

        trains = TrainScheduleSerializer(trains, many=True).data

        return trains
    
    @classmethod
    def get_booking(cls, booking_uuid: str) -> Optional[Dict]:
        booking = Booking.objects.filter(uuid=booking_uuid).first()
        if not booking:
            return None
        
        seats = Seat.objects.filter(booking=booking)
        seats = SeatSerializer(seats, many=True).data

        booking_data = FullBookingDetailsSerializer(booking).data
        booking_data.update({'seats': seats})
        return booking_data
    

    @classmethod
    def add_train(cls, data: Dict[str, str]) -> Optional[Dict]:
        train = Train.objects.create(**data)
        return TrainSerializer(train).data

    @classmethod
    def add_train_schedule(cls, data: Dict[str, str]) -> Optional[Dict]:
        train = Train.objects.filter(train_number=data['train_number']).first()

        data.pop('train_number')
        if not train:
            return None
        
        schedule = TrainSchedule.objects.create(train=train, **data)
        return TrainScheduleSerializer(schedule).data
    
    @classmethod
    def update_train_schedule(cls, schedule_id, data: Dict[str, str]) -> Optional[Dict]:
        schedule = TrainSchedule.objects.filter(id=schedule_id).first()
        if not schedule:
            return None
        
        for key, value in data.items():
            setattr(schedule, key, value)
        
        schedule.save()
        return TrainScheduleSerializer(schedule).data

        

        
        
        