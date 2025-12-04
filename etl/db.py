from streamlit import st
from sqlalchemy import create_engine

def get_engine():
    user = st.secrets["DB_USER"]
    password = st.secrets["DB_PASSWORD"]
    host = st.secrets["POSTGRES_HOST"]
    port = st.secrets["POSTGRES_PORT"]
    db = st.secrets["POSTGRES_DB"]
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url, pool_pre_ping=True)
