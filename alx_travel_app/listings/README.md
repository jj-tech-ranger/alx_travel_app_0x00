# Listings Django App

## Overview

The Listings app is the core application for managing travel property listings, bookings, and reviews in the ALX Travel App platform.

## Features

### Models

#### Listing Model
- Manages property listings with details like name, location, description, and pricing
- Uses UUID as primary key for distributed system compatibility
- Includes automatic timestamps (created_at, updated_at)
- Indexed fields for optimized queries

#### Booking Model
- Handles booking requests with status tracking (pending, confirmed, canceled)
- Establishes ForeignKey relationship with Listing
- Validates date ranges and pricing
- Tracks booking lifecycle with timestamps

#### Review Model  
- Manages user reviews and ratings (1-5 scale)
- Links to listings via ForeignKey
- Enforces rating constraints at database level
- Supports detailed user feedback

### Serializers

Django REST Framework serializers for API integration:

- **ListingSerializer**: Converts Listing model to JSON with validation
- **BookingSerializer**: Handles booking data with date validation
- **ReviewSerializer**: Processes reviews with rating constraints

### Management Commands

#### Database Seeding

Run the seed command to populate the database with sample data:

```bash
python manage.py seed
```

This creates:
- 5 sample property listings
- 3 sample bookings
- 5 sample reviews

## File Structure

```
listings/
├── __init__.py
├── apps.py              # App configuration
├── models.py            # Database models (Listing, Booking, Review)
├── serializers.py       # DRF serializers
├── management/
│   └── commands/
│       └── seed.py      # Database seeding command
└── README.md            # This file
```

## Usage

### Setup

1. Add 'listings' to INSTALLED_APPS in settings.py:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'listings',
]
```

2. Run migrations:
```bash
python manage.py makemigrations listings
python manage.py migrate
```

3. Seed the database (optional):
```bash
python manage.py seed
```

### Database Schema

**Listings Table:**
- listing_id (UUID, PK)
- host_id (UUID)
- name (VARCHAR)
- description (TEXT)
- location (VARCHAR)
- price_per_night (DECIMAL)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

**Bookings Table:**
- booking_id (UUID, PK)  
- listing_id (UUID, FK)
- user_id (UUID)
- start_date (DATE)
- end_date (DATE)
- total_price (DECIMAL)
- status (VARCHAR)
- created_at (TIMESTAMP)

**Reviews Table:**
- review_id (UUID, PK)
- listing_id (UUID, FK)
- user_id (UUID)
- rating (INTEGER, 1-5)
- comment (TEXT)
- created_at (TIMESTAMP)

## API Integration

This app is designed to work with Django REST Framework for API endpoints. The serializers handle:

- Data validation
- JSON serialization/deserialization
- Related field access
- Custom validation rules

## Development

To extend this app:

1. Add new models in `models.py`
2. Create corresponding serializers in `serializers.py`
3. Update management commands as needed
4. Run migrations to update database schema

## Requirements

- Django 3.2+
- Django REST Framework 3.12+
- Python 3.8+

For more information, see the main project README.
