from sqlalchemy import create_engine

def get_engine():
    # Cloud: use Supabase Pooler
    if "DATABASE_URL" in st.secrets:
        return create_engine(st.secrets["DATABASE_URL"], pool_pre_ping=True)

    # Local: use normal Postgres connection
    user = st.secrets["DB_USER"]
    password = st.secrets["DB_PASSWORD"]
    host = st.secrets["POSTGRES_HOST"]
    port = st.secrets["POSTGRES_PORT"]
    db = st.secrets["POSTGRES_DB"]

    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url, pool_pre_ping=True)
