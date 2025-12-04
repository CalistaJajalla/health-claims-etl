import os
from sqlalchemy import create_engine

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url, pool_pre_ping=True)
