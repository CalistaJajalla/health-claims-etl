from sqlalchemy import create_engine
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

def get_engine(secrets):
    # Cloud: use Supabase Pooler URL if available
    if "DATABASE_URL" in secrets:
        url = secrets["DATABASE_URL"]
        # Sanitize URL: remove 'pgbouncer=true' if present
        parsed_url = urlparse(url)
        query_params = dict(parse_qsl(parsed_url.query))
        if 'pgbouncer' in query_params:
            query_params.pop('pgbouncer')
            sanitized_query = urlencode(query_params)
            parsed_url = parsed_url._replace(query=sanitized_query)
            url = urlunparse(parsed_url)
        return create_engine(url, pool_pre_ping=True)

    # Local: use normal Postgres connection from individual secrets
    user = secrets["DB_USER"]
    password = secrets["DB_PASSWORD"]
    host = secrets["POSTGRES_HOST"]
    port = secrets["POSTGRES_PORT"]
    db = secrets["POSTGRES_DB"]

    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url, pool_pre_ping=True)
