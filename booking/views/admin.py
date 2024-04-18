from account.custom_viewset import AdminViewSet
from booking.serializers import TrainSerializer, AddTrainScheduleSerializer, UpdateTrainScheduleSerializer
from utils.response import error_response, success_response
from rest_framework import status
from booking.services.booking import BookingService

class AdminBookingViewSet(AdminViewSet):

    def add_train(self,request):
        serializer = TrainSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(data=serializer.errors,msg="", status=status.HTTP_400_BAD_REQUEST)
        
        train = BookingService.add_train(serializer.validated_data)

        if not train:
            return error_response(msg="Train not added",data={}, status=status.HTTP_400_BAD_REQUEST)
        
        return success_response(status=status.HTTP_201_CREATED,msg="Train added successfully",data=train)

    def add_train_schedule(self,request):
        serializer = AddTrainScheduleSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(data=serializer.errors,msg="", status=status.HTTP_400_BAD_REQUEST)
        
        schedule = BookingService.add_train_schedule(serializer.validated_data)

        if not schedule:
            return error_response(msg="Schedule not added",data={}, status=status.HTTP_400_BAD_REQUEST)
        
        return success_response(status=status.HTTP_201_CREATED,msg="Schedule added successfully",data=schedule)

    def update_train_schedule(self,request, schedule_id):
        serializer = UpdateTrainScheduleSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(data=serializer.errors,msg="", status=status.HTTP_400_BAD_REQUEST)
        
        schedule = BookingService.update_train_schedule(schedule_id, serializer.validated_data)

        if not schedule:
            return error_response(msg="Schedule not updated",data={}, status=status.HTTP_400_BAD_REQUEST)
        
        return success_response(status=status.HTTP_201_CREATED,msg="Schedule updated successfully",data=schedule)