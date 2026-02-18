# PWP SPRING 2026
# LOST AND FOUND
# Group information
- **Student 1:** Ram Sharan Sapkota  
  **Email:** Ram.Sapkota@student.oulu.fi  

- **Student 2:** Sujith Srinivasan  
  **Email:** Sujith.Srinivasan@student.oulu.fi  

- **Student 2:** Mikko Kalliainen  
  **Email:** Mikko.Kalliainen@student.oulu.fi 

__Remember to include all required documentation and HOWTOs, including how to create and populate the database, how to run and test the API, the url to the entrypoint, instructions on how to setup and run the client, instructions on how to setup and run the axiliary service and instructions on how to deploy the api in a production environment__

# Lost and Found System – Database Implementation

## Overview
This project implements the database backend of a Lost and Found system.  
The database stores Users, Found Items, Claim Requests, and Pickup Logs using SQLAlchemy ORM with SQLite.

---

## Technologies
- Python 3.x  
- FastAPI  
- SQLAlchemy  
- Postgres  
- Pydantic
- alembic  

---

## Database
- Database: Postgres  
- Tables are created automatically using SQLAlchemy models.

To create tables and run the app:

## Installation

Create a virtual environment:

```bash
python -m venv venv

Create a virtual environment:

```bash
python -m venv venv

venv\Scripts\activate

## Installation dependencies

pip install -r requirements.txt

# Create initial migration (first time only)
alembic revision --autogenerate -m "initial tables"

# Apply migration to create tables
alembic upgrade head

uvicorn app.main:app --reload




