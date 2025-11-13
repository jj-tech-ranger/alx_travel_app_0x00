from django.db import models
import uuid


class Listing(models.Model):
    """
    Model representing a property listing available for booking.
    """
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host_id = models.UUIDField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'listings'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['host_id']),
            models.Index(fields=['location']),
        ]

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Model representing a booking made by a user for a listing.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    user_id = models.UUIDField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bookings'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['listing']),
            models.Index(fields=['user_id']),
            models.Index(fields=['start_date', 'end_date']),
        ]

    def __str__(self):
        return f"Booking {self.booking_id} for {self.listing.name}"


class Review(models.Model):
    """
    Model representing a review left by a user for a listing.
    """
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user_id = models.UUIDField()
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['listing']),
            models.Index(fields=['user_id']),
            models.Index(fields=['rating']),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                name='rating_range'
            )
        ]

    def __str__(self):
        return f"Review by {self.user_id} for {self.listing.name}"
