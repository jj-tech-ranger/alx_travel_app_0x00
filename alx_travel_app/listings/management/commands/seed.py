from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
import uuid
from datetime import date, timedelta
from decimal import Decimal


class Command(BaseCommand):
    help = 'Seed the database with sample listing, booking, and review data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Clear existing data
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared existing data'))

        # Create sample listings
        listings_data = [
            {
                'host_id': uuid.uuid4(),
                'name': 'Cozy Beach House',
                'description': 'Beautiful beach house with stunning ocean views. Perfect for a relaxing getaway.',
                'location': 'Malibu, California',
                'price_per_night': Decimal('250.00')
            },
            {
                'host_id': uuid.uuid4(),
                'name': 'Mountain Cabin Retreat',
                'description': 'Rustic cabin in the mountains with hiking trails and wildlife.',
                'location': 'Aspen, Colorado',
                'price_per_night': Decimal('180.00')
            },
            {
                'host_id': uuid.uuid4(),
                'name': 'Downtown Luxury Apartment',
                'description': 'Modern apartment in the heart of the city with all amenities.',
                'location': 'New York, New York',
                'price_per_night': Decimal('350.00')
            },
            {
                'host_id': uuid.uuid4(),
                'name': 'Tropical Paradise Villa',
                'description': 'Luxurious villa with private pool and tropical gardens.',
                'location': 'Miami, Florida',
                'price_per_night': Decimal('450.00')
            },
            {
                'host_id': uuid.uuid4(),
                'name': 'Historic Victorian Home',
                'description': 'Charming Victorian home with period features and modern comforts.',
                'location': 'San Francisco, California',
                'price_per_night': Decimal('200.00')
            },
        ]

        listings = []
        for data in listings_data:
            listing = Listing.objects.create(**data)
            listings.append(listing)
            self.stdout.write(f'Created listing: {listing.name}')

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(listings)} listings'))

        # Create sample bookings
        user_ids = [uuid.uuid4() for _ in range(3)]
        bookings = []
        
        for i, listing in enumerate(listings[:3]):
            start_date = date.today() + timedelta(days=(i + 1) * 7)
            end_date = start_date + timedelta(days=3)
            total_price = listing.price_per_night * 3
            
            booking = Booking.objects.create(
                listing=listing,
                user_id=user_ids[i % len(user_ids)],
                start_date=start_date,
                end_date=end_date,
                total_price=total_price,
                status='confirmed'
            )
            bookings.append(booking)
            self.stdout.write(f'Created booking for: {listing.name}')

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(bookings)} bookings'))

        # Create sample reviews
        reviews_data = [
            {
                'listing': listings[0],
                'user_id': user_ids[0],
                'rating': 5,
                'comment': 'Amazing place! The ocean view was breathtaking and the host was very accommodating.'
            },
            {
                'listing': listings[1],
                'user_id': user_ids[1],
                'rating': 4,
                'comment': 'Great cabin for a mountain getaway. Very peaceful and well-maintained.'
            },
            {
                'listing': listings[2],
                'user_id': user_ids[2],
                'rating': 5,
                'comment': 'Perfect location in downtown! Walking distance to everything we wanted to see.'
            },
            {
                'listing': listings[0],
                'user_id': user_ids[1],
                'rating': 5,
                'comment': 'Would definitely stay here again. The beach access was incredible!'
            },
            {
                'listing': listings[3],
                'user_id': user_ids[0],
                'rating': 4,
                'comment': 'Beautiful villa with amazing pool. Tropical gardens were stunning.'
            },
        ]

        reviews = []
        for review_data in reviews_data:
            review = Review.objects.create(**review_data)
            reviews.append(review)
            self.stdout.write(f'Created review for: {review.listing.name}')

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(reviews)} reviews'))
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))
        self.stdout.write(f'\nSummary:')
        self.stdout.write(f'  - Listings: {len(listings)}')
        self.stdout.write(f'  - Bookings: {len(bookings)}')
        self.stdout.write(f'  - Reviews: {len(reviews)}')
