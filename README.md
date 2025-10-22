# Hospital Officio - Patient Management System

A modern, responsive patient management system built with Django featuring beautiful glassmorphism design and comprehensive patient tracking capabilities.

## 🏥 Features

## 🔐 Authentication System

User Registration - Secure account creation with validation

User Login - Authentication with session management

Profile Management - Update personal information and passwords

Password Recovery - Secure password reset functionality


## 👥 Patient Management
Create Patients - Add new patient records with comprehensive details

View Patients - Beautiful card-based patient display

Update Patients - Modify existing patient information

Delete Patients - Remove patient records with confirmation

Search Functionality - Find patients by name, doctor, room, age, or disease

Doctor Assignment - Track doctor-patient relationships

Room Management - Monitor patient room assignments

## 🎨 Modern UI/UX
Glassmorphism Design - Beautiful translucent glass-like elements

Responsive Layout - Works perfectly on all device sizes

Smooth Animations - Elegant transitions and hover effects

Modern Color Scheme - Professional blue gradient theme

Interactive Elements - Hover effects and micro-interactions

## 🛠️ Technology Stack
Backend: Django 4.2

Frontend: HTML5, CSS3, JavaScript

Styling: Custom CSS with Glassmorphism effects

Database: SQLite (default)

## 🔒 Security Features
Password Hashing: Secure password storage

Session Management: Protected user sessions

Input Validation: Form data validation

Authentication Required: Protected views for authenticated users only

CSRF Protection: Cross-site request forgery protection

## 🎯 Core Functionality
### Patient Management (base/views.py)

Home: Landing page dashboard

Create Patient: Add new patient records

Display Patients: View all patients with search

Update Patient: Modify patient information

Delete Patient: Remove patient records

### Authentication (authen/views.py)

Sign Up: User registration

Sign In: User login

Profile: User profile management

Update Profile: Edit user information

Update Password: Change user password

Forgot Password: Password recovery system

Sign Out: User logout

Authentication: Django built-in auth system

Icons: Unicode emojis and symbols

## 🚀 Installation & Setup

### 1. Clone the repository

git clone https://github.com/s01dier-0f-g0d/hospital_manager.git

cd hospital-officio

### 3. Create virtual environment

python -m venv venv

On Mac OS: source venv/bin/activate

(OR)

On Windows: venv\Scripts\activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Run migrations

python manage.py migrate

### 6. Create superuser

python manage.py createsuperuser

### 7. Run development server

python manage.py runserver

### 8. Access the application

http://localhost:8000
