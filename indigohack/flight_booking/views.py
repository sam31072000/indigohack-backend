from rest_framework.views import APIView
from flight_booking.controllers import BookFlightController, ListBookFlightsController
from rest_framework.response import Response
from rest_framework import status
from flight_booking.serializers import BookFlightSerializer

class BookFlightView(APIView):

    def post(self, request):
        validator = BookFlightSerializer(data=request.data)
        success = validator.is_valid(raise_exception=True)
        validated_data = validator.validated_data
        response = BookFlightController(data=validated_data).book_flight()
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request):
        validator = BookFlightSerializer(data=request.data)
        success = validator.is_valid(raise_exception=True)
        validated_data = validator.validated_data
        response = BookFlightController(data=validated_data).book_flight()
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, booking_id):
        data = {
            "booking_id": booking_id
        }
        response = BookFlightController(data=data).cancel_booking()
        return Response(response, status=status.HTTP_200_OK)
    
    def get(self, request):
        validator = BookFlightSerializer(data=request.data)
        success = validator.is_valid(raise_exception=True)
        validated_data = validator.validated_data
        response = ListBookFlightsController(data=validated_data).list_bookings()
        return Response(response, status=status.HTTP_200_OK)
    