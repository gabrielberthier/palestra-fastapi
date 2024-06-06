from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True


class PlayerCreate(BaseModel):
    name: str
    level: int = Field(..., gt=0)
    user_id: int = Field(..., gt=0)


class Player(BaseModel):
    id: int
    name: str
    level: int = Field(..., gt=0)
    user_id: int = Field(..., gt=0)  

    user: User
