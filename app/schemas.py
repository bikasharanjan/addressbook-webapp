from pydantic import BaseModel, Field, confloat
from typing import Optional
from datetime import datetime

class AddressBase(BaseModel):
    name: str = Field(..., example="Home")
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    name: Optional[str]
    latitude: Optional[confloat(ge=-90, le=90)]
    longitude: Optional[confloat(ge=-180, le=180)]

class AddressOut(AddressBase):
    id: int
    created_at: Optional[datetime]
    class Config:
        orm_mode = True
