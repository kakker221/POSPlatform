import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SECURE = True  # Ensures cookies are only sent over HTTPS
    SESSION_COOKIE_HTTPONLY = True  # Prevents JavaScript from accessing the cookies
    SESSION_COOKIE_SAMESITE = 'Lax'  # Mitigates CSRF by restricting cross-site requests
    
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY', 'another_random_secret_key')
    WTF_CSRF_ENABLED = True

    print(f'Secret key: {SECRET_KEY}')
    print(f'Database URI: {SQLALCHEMY_DATABASE_URI}')