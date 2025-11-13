# ALX Travel App

## Django Application Directory

This directory contains the Django application for the travel listing platform.

### Structure

```
alx_travel_app/
└── listings/          # Main listings application
    ├── models.py      # Database models
    ├── serializers.py # DRF serializers
    ├── management/    # Management commands
    └── ...
```

### Listings Application

The `listings` app handles:
- Property listing management
- Booking system
- Review system
- Database seeding

### Setup

To use this application:

1. Ensure Django and DRF are installed
2. Add 'listings' to INSTALLED_APPS in settings.py
3. Run migrations: `python manage.py migrate`
4. Seed database: `python manage.py seed`

For more information, see the main project README.md
