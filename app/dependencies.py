from dotenv import load_dotenv
import os 

load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))

from app.infra.db.base import SessionLocal, engine
from app.infra.models import Base

Base.metadata.create_all(bind=engine)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()