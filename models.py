from pydantic import BaseModel
from enum import Enum

class Genre(str, Enum):
    FANTASY = "FANTASY"
    ROMANCE = "ROMANCE"
    SCIFI = "SCIFI"

class Book(BaseModel):
    genre: Genre
    price: float
    stock_count: int
