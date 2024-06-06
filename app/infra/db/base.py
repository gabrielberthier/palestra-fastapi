from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from os import environ

user = environ.get("POSTGRES_USER")
db = environ.get("POSTGRES_DB")
userpass = environ.get("POSTGRES_PASSWORD")

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
POSTGRESQL_DATABASE_URL = f"postgresql+psycopg2://{user}:{userpass}@db/{db}"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
engine = create_engine(POSTGRESQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
