import os
from sqlalchemy import create_engine

def get_engine():
    user = os.getenv("DB_USER", "user")
    password = os.getenv("DB_PASSWORD", "password")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "health_claims")
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return engine
