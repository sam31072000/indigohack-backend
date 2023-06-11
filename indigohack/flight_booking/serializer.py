from rest_framework import serializers

class BookFlightSerializer(serializers.Serializer):

    booking_type = [
        "ONE_WAY",
        "ROUND_TRIP",
        "MULTI_WAY"
    ]

    booking_type = serializers.ChoiceField(required=False, choices=booking_type)
    flight_id = serializers.IntegerField(required=True, allow_null=False)
    num_of_passengers = serializers.IntegerField(required=True, allow_null=False, min_value=1)
    contact_phone_number = serializers.CharField(required=True, min_length=10, max_length=10)
    contact_email = serializers.EmailField(required=False)


class EditBookFlightSerializer(serializers.Serializer):

    booking_type = [
        "ONE_WAY",
        "ROUND_TRIP",
        "MULTI_WAY"
    ]
    booking_id = serializers.IntegerField(required=True, allow_null=False)
    booking_type = serializers.ChoiceField(required=False, choices=booking_type)
    num_of_passengers = serializers.IntegerField(required=True, allow_null=False, min_value=1)
    contact_phone_number = serializers.CharField(required=True, min_length=10, max_length=10)
    contact_email = serializers.EmailField(required=False)

class ListBookingsSerializer(serializers.Serializer):
    booking_status = ["SUCCESS", "CANCELLED", "COMPLETED"]
    booking_status = serializers.ChoiceField(required=False, choices=booking_status)

    def to_representation(self, instance):

        data = {
            "booking_id": instance.id,
            "origin": instance.source_place_name,
            "destination": instance.destination_place_name,
            "departure": instance.departure_time,
            "booked_on": instance.booked_on,
            "return_on": instance.return_on
        }