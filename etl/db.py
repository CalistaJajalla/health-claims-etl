import os
from sqlalchemy import create_engine

def get_engine():
    user = st.secrets["postgres"]["user"]
    password = st.secrets["postgres"]["password"]
    host = st.secrets["postgres"]["host"]
    port = st.secrets["postgres"]["port"]
    db = st.secrets["postgres"]["database"]
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(url, pool_pre_ping=True)
    return engine

