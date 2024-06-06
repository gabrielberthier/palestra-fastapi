from app.infra.db.base import SessionLocal


# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
