# Django Intern Assignment – Vendor Product Course Certification API

## Project Overview

This project is a **Django REST Framework backend API** built using **APIView only**.
The system manages the following entities:

- Vendor
- Product
- Course
- Certification

It also manages relationships between these entities using mapping tables.

### Mapping Relationships

- Vendor → Product
- Product → Course
- Course → Certification

The project follows a **modular Django architecture** where each entity and mapping has its own Django app.

---

# Technology Stack

- Python
- Django
- Django REST Framework
- drf-yasg (Swagger Documentation)
- SQLite Database

---

# Project Structure

```text
myproject
│
├── vendor
├── product
├── course
├── certification
│
├── vendor_product_mapping
├── product_course_mapping
├── course_certification_mapping
│
├── seed_data
│   └── management
│        └── commands
│             └── seed_all_data.py
│
├── manage.py
└── README.md
```

---

# Installation Guide

### 1. Clone Repository

```bash
git clone https://github.com/Ranjandas1/djangoassignment.git
cd myproject
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment

Linux / Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install django djangorestframework drf-yasg
```

---

### 4. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Run the Project

Start the development server:

```bash
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000
```

---

# Swagger API Documentation

Swagger UI

```
http://127.0.0.1:8000/swagger/
```

ReDoc

```
http://127.0.0.1:8000/redoc/
```

---

# Load Sample Data

Run seed command:

```bash
python manage.py seed_all_data
```

This command will populate the database with sample:

- Vendors
- Products
- Courses
- Certifications

---

# API Endpoints

## Vendor APIs

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | /api/vendors/      |
| POST   | /api/vendors/      |
| GET    | /api/vendors/{id}/ |
| PUT    | /api/vendors/{id}/ |
| PATCH  | /api/vendors/{id}/ |
| DELETE | /api/vendors/{id}/ |

---

## Product APIs

| Method | Endpoint            |
| ------ | ------------------- |
| GET    | /api/products/      |
| POST   | /api/products/      |
| GET    | /api/products/{id}/ |
| PUT    | /api/products/{id}/ |
| PATCH  | /api/products/{id}/ |
| DELETE | /api/products/{id}/ |

---

## Course APIs

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | /api/courses/      |
| POST   | /api/courses/      |
| GET    | /api/courses/{id}/ |
| PUT    | /api/courses/{id}/ |
| PATCH  | /api/courses/{id}/ |
| DELETE | /api/courses/{id}/ |

---

## Certification APIs

| Method | Endpoint                  |
| ------ | ------------------------- |
| GET    | /api/certifications/      |
| POST   | /api/certifications/      |
| GET    | /api/certifications/{id}/ |
| PUT    | /api/certifications/{id}/ |
| PATCH  | /api/certifications/{id}/ |
| DELETE | /api/certifications/{id}/ |

---

# Query Filtering

Examples

```
/api/products/?vendor_id=1
/api/courses/?product_id=2
/api/certifications/?course_id=3
```

---

# Features Implemented

- Modular Django apps
- CRUD APIs using APIView
- Serializer validation
- Query parameter filtering
- Duplicate mapping prevention
- Swagger API documentation
- Seed script for sample data
