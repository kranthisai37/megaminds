# PixelForge – Role-Based Project Management System

## 📌 Project Overview

PixelForge is a role-based project management system built using Django.  
The system allows Admins, Project Leads, and Developers to collaborate securely with controlled access permissions and document management.

This project demonstrates authentication, authorization, object-level access control, and secure file handling.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- Custom User Model extending AbstractUser
- Role-Based Access Control (Admin, Lead, Developer)
- Secure Login & Logout (POST-based logout for Django 6 security compliance)
- Password hashing using Django’s built-in authentication system

---

### 🗂 Project Management
- Admin can create projects
- Admin assigns Project Leads
- Leads can assign Developers to their projects
- Many-to-Many relationship between Projects and Developers

---

### 📄 Secure Document Management
- Admin & Lead can upload project documents
- Developers can view only documents of assigned projects
- Object-level permission checks implemented
- Secure file handling using Django’s `request.FILES`

---

### 🎨 User Interface
- Responsive UI built using Bootstrap 5
- Card-based dashboard design
- Role-based action visibility
- Clean and consistent layout

---

## 🏗 Tech Stack

- Python 3
- Django 6
- SQLite
- Bootstrap 5

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd pixelforge
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  (Windows)
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 👥 User Roles

| Role       | Permissions |
|------------|------------|
| Admin      | Create projects, assign leads, upload documents |
| Lead       | Assign developers, upload documents (own projects only) |
| Developer  | View assigned projects and documents |

---

## 🔐 Security Implementation

- Custom user model with role field
- Decorator-based role restriction
- Object-level access validation
- POST-based logout enforcement
- Secure password hashing via Django UserAdmin
- Restricted document access per project assignment

---

## 📁 Project Structure

```
pixelforge/
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🎯 Key Learning Outcomes

- Custom authentication system
- Role-based access control
- Many-to-Many relationships
- Object-level permission handling
- Secure file upload implementation
- Bootstrap UI integration with Django

---

## 📌 Future Improvements

- Document delete functionality
- Project status tracking enhancements
- Dashboard statistics
- Search & filtering
- Deployment to production server

---

## 👨‍💻 Author

Kranthi  
Fullstack Internship Candidate  