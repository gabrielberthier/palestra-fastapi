from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.domain import schemas
from app.infra import crud

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/players/", response_model=schemas.Player)
def create_player(player_object: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=player_object.user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    return crud.create_user_player(db=db, player=player_object)


@app.get("/players/{user_id}", response_model=schemas.Player)
def get_players(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_player(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
