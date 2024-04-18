from account.custom_viewset import UserViewSet
from booking.serializers import BookSeatSerializer, TrainScheduleRequestSerializer
from utils.response import error_response, success_response
from rest_framework import status

from booking.services.booking import BookingService

class BookingViewSet(UserViewSet):
    
    def create_booking(self,request):
        """Create booking view"""
        serializer = BookSeatSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(data=serializer.errors,msg="", status=status.HTTP_400_BAD_REQUEST) 
        
        # import pdb; pdb.set_trace()

        booking, message = BookingService.create_booking(request.user, serializer.validated_data)

        if not booking:
            return error_response(msg=message,data={}, status=status.HTTP_400_BAD_REQUEST)

        return success_response(status=status.HTTP_201_CREATED,msg= message,data= booking)   
    
    def get_trains(self,request):
        """Get all trains view"""
        serializer = TrainScheduleRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(data=serializer.errors,msg="", status=status.HTTP_400_BAD_REQUEST)
        
        trains = BookingService.get_trains(serializer.validated_data)

        if not trains:
            return error_response(msg="No trains found",data={}, status=status.HTTP_400_BAD_REQUEST)

        return success_response(status=status.HTTP_200_OK,msg="Trains fetched successfully",data=trains)
        
    
    def get_booking(self,request, booking_uuid):
        """Get booking view"""
        bookings = BookingService.get_booking(booking_uuid)
        return success_response(status=status.HTTP_200_OK,msg="Booking fetched successfully",data=bookings)