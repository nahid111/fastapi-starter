from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

db_user = settings.POSTGRES_USER
db_pass = settings.POSTGRES_PASSWORD
db_host = settings.POSTGRES_HOSTNAME
db_port = settings.DATABASE_PORT
db_name = settings.POSTGRES_DB

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
