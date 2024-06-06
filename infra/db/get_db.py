from infra.models import Base
from infra.db.base import SessionLocal, engine

Base.metadata.create_all(bind=engine)

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()