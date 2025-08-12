# -------------------------------
# README.md
# -------------------------------

# 📍 Address Book API (FastAPI)

A simple Address Book web API built with **FastAPI** and **SQLite**.  
It allows users to store, update, delete, and search addresses by distance using latitude & longitude.

---

## 🚀 Features
- Add, update, delete, and view addresses
- Search for addresses within a given distance
- Uses **Haversine formula** to calculate distances between coordinates
- OpenAPI documentation (Swagger UI) built-in
- SQLite database (easy local setup)
- Environment-based configuration with `.env`

---

## 📦 Tech Stack
- **Python 3.9+**
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

---

## 📂 Project Structure
addressbook-webapp/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── utils.py
│   └── routes/
│       └── address.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/<your-username>/addressbook-webapp.git
cd addressbook-webapp

### 2️⃣ Create & activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Create `.env` file
DATABASE_URL=sqlite:///./addresses.db

### 5️⃣ Run the app
uvicorn app.main:app --reload

---

## 📑 API Documentation
Once running, open:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 📌 Example API Calls

### Add an Address
POST /addresses/
Content-Type: application/json

{
  "name": "Home",
  "latitude": 28.6139,
  "longitude": 77.2090
}

### Get All Addresses
GET /addresses/

### Find Addresses Within Distance
GET /addresses/within?lat=28.6&lon=77.2&dist_km=5

---

# -------------------------------
# .gitignore
# -------------------------------

# Virtual env
venv/
ENV/
env/
.venv/

# Environment files
.env

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# SQLite database
addresses.db

# OS / Editor files
.vscode/
.idea/
.DS_Store
Thumbs.db

# Logs
*.log
