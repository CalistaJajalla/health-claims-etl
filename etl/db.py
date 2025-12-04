import os
from sqlalchemy import create_engine

def get_engine():
    user = st.secrets["DB_USER"]
    password = st.secrets["DB_PASSWORD"]
    host = st.secrets["POSTGRES_HOST"]
    port = st.secrets["POSTGRES_PORT"]
    db = st.secrets["POSTGRES_DB"]
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(url)
    return engine
