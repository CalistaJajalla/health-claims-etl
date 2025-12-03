import os
from sqlalchemy import create_engine

def get_engine():
    user = 'user'
    password = 'password'
    host = os.getenv('POSTGRES_HOST', 'localhost')
    port = '5432'
    db = 'health_claims'
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    engine = create_engine(url, pool_pre_ping=True)
    return engine

