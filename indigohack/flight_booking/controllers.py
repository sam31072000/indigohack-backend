from flight_booking.models import BookingModel, FlightsModel
from libs.api_exception import CustomError
from flight_booking.serializers import ListBookingsSerializer


class BookFlightController:

    def __init__(self, **kwargs):
        self.data = kwargs.get('data')

    def book_flight():
        """
        Controller to book a flight
        """
        flight_obj = None
        try:
            obj = FlightsModel.objects.get(id=id)
            flight_obj = obj
        except self.model.DoesNotExist:
            pass
        
        if not flight_obj:
            raise CustomError({"status": 0, "message": "Flight Not Found"},400)

        payload = {
            "booking_type": self.data.get("booking_type"),
            "flight_id": self.data.get("flight_id"),
            "num_of_passengers": self.data.get("num_of_passengers"),
            "contact_phone_number": self.data.get("contact_phone_number"),
            "contact_email": self.data.get("contact_email"),
            "booking_status": "SUCCESS"
        }
        BookingModel.objects.create(**payload)
        
        #TODO
        #Payment Status

        response_data = {
            "data": "Flight Successfully Booked"
        }
        return response_data
    
    def edit_flight(self):
        """
        Controller to Edit a flight.
        Note:- Flight Id is non editable field
        """
        booking_obj = None

        try:
            obj = BookingModel.objects.get(id=self.data.get("booking_id"))
            booking_obj = obj
        except self.model.DoesNotExist:
            pass
        
        if not booking_obj:
            raise CustomError({"status": 0, "message": "Booking Not Found"},400)
        
        #We can also maintain logs here

        booking_obj.booking_type = self.data.get("booking_type")
        booking_obj.num_of_passengers = self.data.get("num_of_passengers")
        booking_obj.contact_phone_number = self.data.get("contact_phone_number")
        booking_obj.contact_email = self.data.get("contact_email")
        
        booking_obj.save()

        response_data = {
            "data": "Flight Successfully Updated"
        }
        return response_data

    def cancel_booking(self):
        """
        Controller to Cancel a flight
        """
        booking_obj = None

        try:
            obj = BookingModel.objects.get(id=self.data.get("booking_id"))
            booking_obj = obj
        except self.model.DoesNotExist:
            pass
        
        if not booking_obj:
            raise CustomError({"status": 0, "message": "Booking Not Found"},400)
        
        booking_obj.status = "CANCELLED"
        booking_obj.save()

        #TODO
        #Initiate Refund Here

        response_data = {
            "data": "Booking Successfully Cancelled"
        }
        return response_data

    
class ListBookFlightsController:

    def __init__(self, **kwargs):
        self.data = kwargs.get("data")

    
    def list_bookings(self):
        filters = {}

        if self.data.get("booking_status"):
            filters["booking_status"] = self.data.get("booking_status")

        booking_qset = BookingModel.models.filters(**filters)
        total_bookings = 0

        if booking_qset.exists():
            total_bookings = booking_qset.count()

        serialized_data = ListBookingsSerializer(booking_qset, many=True).data
        
        response_data = {
            "data": {
                "results": serialized_data,
                "total": total_bookings
            }
        }

        return response_data