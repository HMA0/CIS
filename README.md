Module 1 - Authentication & Driver Verification (FastAPI)

Contents:
- auth routes (register/login)
- user model and driver documents model
- driver docs upload endpoints (save to uploads/drivers)
- security utils (JWT, password hashing)
- simple SQLite setup for quick testing

Usage:
1. python -m venv venv && source venv/bin/activate
2. pip install -r requirements.txt
3. cp .env.example .env
4. uvicorn app.main:app --reload
5. Open /docs for API
