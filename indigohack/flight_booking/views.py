from rest_framework.views import APIView
from flight_booking.controllers import BookFlightController
from rest_framework.response import Response
from rest_framework import status

class BookFlightView(APIView):

    def post(self, request):
        response = BookFlightController().book_flight()

        return Response(response, status=status.HTTP_200_OK)
    