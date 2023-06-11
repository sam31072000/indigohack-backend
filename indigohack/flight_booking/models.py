from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,None=True)
	updated_at = models.DateTimeField(auto_now=True,None=True)
	is_active = models.BooleanField(default=True)

class BookingModel(AbstractModel):

    booking_type = (
        ("ONE_WAY", "ONE_WAY"),
        ("ROUND_TRIP", "ROUND_TRIP"),
        ("MULTI_WAY", "MULTI_WAY"),
    )

    success_status = (
        ("SUCCESS", "SUCCESS"),
        ("FAILED", "FAILED"),
        ("CANCELLED", "CANCELLED"),
    )

    booking_type = models.CharField(max_length=50, choices=booking_type, default=None, None=True, blank=False)
    flight_id = models.IntegerField(default=None, None=True, blank=False)
    num_of_passengers = models.IntegerField(default=None, None=True, blank=False)
    contact_phone_number = models.CharField(max_length=10, default=None, None=True, blank=False)
    booking_status = models.CharField(max_length=10, choices=success_status, default=None, None=True, blank=False)
    payment_status = models.CharField(max_length=10, choices=success_status, default=None, None=True, blank=False)
    booked_on = models.DateTimeField(auto_now=True,None=True)

class FlightsModel(AbstractModel):
    destination_place_id = models.IntegerField(default=None, None=True, blank=False)
    source_place_id = models.IntegerField(default=None, None=True, blank=False)
    departure_time = models.DateTimeField(default=None, None=True, blank=False)
    arrival_time = models.DateTimeField(default=None, None=True, blank=False)
    available_seats = models.IntegerField(default=None, None=True, blank=False)

