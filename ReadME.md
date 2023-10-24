# Django Emissions Project

This project is a Django-based web application that tracks emissions data. The data model `Emissions` captures various scopes of emissions, and the project exposes API endpoints for data manipulation and retrieval.

## Features

- **Django Admin Panel**: A web interface for administrators to manually add, update, and view emissions data.
- **RESTful API**: Exposes endpoints for CRUD operations on the `Emissions` data.
- **Swagger Documentation**: Provides a user-friendly interface to understand and test the API.

## Setup

1.Clone the Repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
   
2.Install Dependencies:
   ```bash
    pip install -r requirements.txt
   ``` 

3.Initialize the Database:
   ```bash
    python manage.py migrate
   ```


4.Run the Development Server:
   ```bash
    python manage.py runserver
   ```

5.Access the Admin Panel:
   ```bash
    Navigate to http://127.0.0.1:8000/admin/.
    Log in and manage the Emissions data.
   ```

6.Access the Swagger Documentation:
   ```bash
    Navigate to `http://127.0.0.1:8000/swagger/`.
    Explore and test the API endpoints.
   ```
   
## API Endpoints

- **List & Create Emissions**: `GET` & `POST` `/emissions/`
- Additional endpoints can be explored via the Swagger documentation.
