# Django Project

## Prerequisites
Ensure you have the following installed on your system:
- Python (==3.11.9)
- pip
- Virtualenv (optional but recommended)
- Git

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rahulsanjay009/remarcable_rahul_2025.git
cd remarcable_rahul_2025
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# Activate the virtual environment:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
#### Using SQLite (default Django DB):
No additional setup is required.

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin Panel Access)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin user.

### 7. Run the Development Server
```bash
python manage.py runserver
```
The application should be running at `http://127.0.0.1:8000/`.

## Troubleshooting
If you encounter issues, check:
- That virtual environment is activated.
- That database credentials are correct.
- That all required dependencies are installed with `pip install -r requirements.txt`.

---
