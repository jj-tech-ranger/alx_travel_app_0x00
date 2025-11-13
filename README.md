# alx_travel_app_0x00

## Django Travel Listing Application

### Project Overview
This Django application provides a complete backend system for managing travel property listings, bookings, and reviews. It includes database models, REST API serializers, and automated database seeding functionality.

### Features
- **Listing Management**: Create and manage property listings with details like location, price, and descriptions
- **Booking System**: Handle booking requests with date validation and status tracking
- **Review System**: Allow users to rate and review properties with rating constraints (1-5)
- **Database Seeding**: Automated command to populate the database with sample data
- **REST API Ready**: Django REST Framework serializers for API integration

### Technology Stack
- **Backend Framework**: Django
- **API Framework**: Django REST Framework (DRF)
- **Database**: SQLite (default) / PostgreSQL
- **Python**: 3.8+

### Project Structure
```
alx_travel_app_0x00/
├── alx_travel_app/
│   └── listings/
│       ├── __init__.py
│       ├── apps.py
│       ├── models.py              # Database models (Listing, Booking, Review)
│       ├── serializers.py         # DRF serializers
│       ├── management/
│       │   └── commands/
│       │       └── seed.py        # Database seeding command
│       └── ...
└── README.md
```

### Models

#### Listing
- `listing_id`: UUID (Primary Key)
- `host_id`: UUID
- `name`: Property name
- `description`: Detailed description
- `location`: Property location
- `price_per_night`: Decimal price
- `created_at`: Timestamp
- `updated_at`: Timestamp

#### Booking
- `booking_id`: UUID (Primary Key)
- `listing`: ForeignKey to Listing
- `user_id`: UUID
- `start_date`: Check-in date
- `end_date`: Check-out date
- `total_price`: Total booking cost
- `status`: Choices (pending, confirmed, canceled)
- `created_at`: Timestamp

#### Review
- `review_id`: UUID (Primary Key)
- `listing`: ForeignKey to Listing
- `user_id`: UUID
- `rating`: Integer (1-5)
- `comment`: Review text
- `created_at`: Timestamp

### Installation & Setup

#### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

#### Step 1: Clone the Repository
```bash
git clone https://github.com/jj-tech-ranger/alx_travel_app_0x00.git
cd alx_travel_app_0x00
```

#### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Step 3: Install Dependencies
```bash
pip install django djangorestframework
```

#### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Step 5: Seed the Database
```bash
python manage.py seed
```

This command will:
- Clear existing data
- Create 5 sample listings
- Create 3 sample bookings
- Create 5 sample reviews

### Running the Application

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Database Seeding Details

The `seed` management command populates the database with realistic sample data:

**Sample Listings Include:**
- Cozy Beach House (Malibu, California)
- Mountain Cabin Retreat (Aspen, Colorado)
- Downtown Luxury Apartment (New York, New York)
- Tropical Paradise Villa (Miami, Florida)
- Historic Victorian Home (San Francisco, California)

Each listing includes:
- Unique host ID
- Detailed description
- Location information
- Competitive pricing

### API Serializers

The application includes three main serializers:

1. **ListingSerializer**: Handles listing data with price validation
2. **BookingSerializer**: Manages bookings with date validation
3. **ReviewSerializer**: Processes reviews with rating constraints

All serializers include:
- Field validation
- Read-only fields for IDs and timestamps
- Related field access (e.g., `listing_name` in bookings)

### Development

#### Running Tests
```bash
python manage.py test
```

#### Creating Superuser
```bash
python manage.py createsuperuser
```

#### Accessing Admin Panel
Navigate to `http://127.0.0.1:8000/admin/` after creating a superuser

### Learning Objectives

This project demonstrates:
- Django model relationships (ForeignKey, OneToMany)
- UUID primary keys for distributed systems
- Database constraints and validation
- DRF serializer implementation
- Custom management commands
- Database seeding best practices

### Key Concepts

- **Relational Data Modeling**: Proper use of ForeignKey relationships
- **Data Validation**: Field-level and object-level validation
- **API Serialization**: Converting Django models to JSON
- **Database Seeding**: Programmatic data population
- **Django ORM**: Efficient database queries with indexing

### Project Requirements

**Required Files:**
- `listings/models.py` - Database model definitions
- `listings/serializers.py` - DRF serializers
- `listings/management/commands/seed.py` - Seeding command
- `README.md` - Project documentation

### Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### License

This project is created for educational purposes as part of the ALX Backend Development curriculum.

### Author

jj-tech-ranger

### Acknowledgments

- ALX Africa Backend Development Program
- Django Documentation
- Django REST Framework Documentation

---

**Project Deadline**: November 17, 2025

**Manual QA Review**: Required upon completion
