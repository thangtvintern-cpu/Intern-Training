# User Management API

Backend service for user authentication and authorization using JWT,
built with FastAPI following Clean Architecture principles.


# Features

- User registration and login
- JWT authentication
- Role-based access control
- User management
- Redis caching

# The project follows Clean Architecture:

- API layer (FastAPI routers)
- Application layer (use cases / services)
- Domain layer (entities, interfaces)
- Infrastructure layer (DB, Redis, external services)

Request
  ↓
Router → Service → Repository → DB

# API Documentation

- http://localhost:8000/docs
- http://localhost:8000/redoc

# Create Virtual Environment

- python -m venv .venv
- .venv\Scripts\Activate

# Install Dependencies

- pip install -r requirements.txt

# Run Project

- uvicorn main:app --reload







