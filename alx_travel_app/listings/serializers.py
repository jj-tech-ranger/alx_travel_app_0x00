from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    Converts Listing instances to JSON for API responses.
    """
    class Meta:
        model = Listing
        fields = [
            'listing_id',
            'host_id',
            'name',
            'description',
            'location',
            'price_per_night',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['listing_id', 'created_at', 'updated_at']

    def validate_price_per_night(self, value):
        """
        Ensure price per night is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Price per night must be greater than zero.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Converts Booking instances to JSON for API responses.
    """
    listing_name = serializers.CharField(source='listing.name', read_only=True)
    listing_location = serializers.CharField(source='listing.location', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'listing',
            'listing_name',
            'listing_location',
            'user_id',
            'start_date',
            'end_date',
            'total_price',
            'status',
            'created_at'
        ]
        read_only_fields = ['booking_id', 'created_at']

    def validate(self, data):
        """
        Validate that end_date is after start_date.
        """
        if data.get('end_date') and data.get('start_date'):
            if data['end_date'] <= data['start_date']:
                raise serializers.ValidationError(
                    "End date must be after start date."
                )
        return data

    def validate_total_price(self, value):
        """
        Ensure total price is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Total price must be greater than zero.")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    Converts Review instances to JSON for API responses.
    """
    listing_name = serializers.CharField(source='listing.name', read_only=True)

    class Meta:
        model = Review
        fields = [
            'review_id',
            'listing',
            'listing_name',
            'user_id',
            'rating',
            'comment',
            'created_at'
        ]
        read_only_fields = ['review_id', 'created_at']

    def validate_rating(self, value):
        """
        Ensure rating is between 1 and 5.
        """
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
