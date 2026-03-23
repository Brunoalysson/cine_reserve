# CineReserve API

CineReserve is a RESTful API for cinema management, allowing users to view movies, sessions, seats, and reserve tickets.  
The backend is built with **Django 5.2**, **Django REST Framework**, and uses **JWT authentication**.

---

## **Technologies Used**

- Python 3.10
- Django 5.2
- Django REST Framework
- PostgreSQL or SQLite (development)
- JWT Authentication
- Postman for API documentation

---

## **Features**

- User registration and login with JWT
- List and create movies
- List and create sessions
- Seat map visualization and temporary seat reservation
- Mandatory pagination for all list-based endpoints
- Checkout and ticket generation (Not finished)
- User ticket listing (Not finished)


---

## **Installation & Local Setup**

### 1. Clone the repository
#bash
git clone https://github.com/Brunoalysson/cine_reserve.git

cd cine_reserve

### 2. Create and activate virtual environment with Poetry
python -m poetry install

python -m poetry shell

### 3. Run Django migrations
python -m poetry run python manage.py migrate

### 4. Create a superuser (admin)
python -m poetry run python manage.py createsuperuser

### 5. Start the development server
python -m poetry run python manage.py runserver

The API will be available at: http://127.0.0.1:8000/

Main API Endpoints:

#Auth


POST /api/token/ – Obtain JWT token

POST /api/token/refresh/ – Refresh JWT token

POST /api/register/ – Register a new user


#Movies

GET /api/movies/ – List movies

POST /api/movies/ – Create a movie (admin only)


#Sessions

GET /api/sessions/ – List sessions

POST /api/sessions/ – Create a session (admin only)


#Seats

GET /api/seats/?session=<id> – List seats for a session

POST /api/seats/{id}/reserve/ – Reserve a seat

All protected endpoints require the header:

Authorization: Bearer <access_token>

**Postman**

You can import the provided Postman collection to easily test all endpoints.

Suggested environment variables:

base_url = http://127.0.0.1:8000

token = <access_token>

refresh_token = <refresh_token>
