from pydantic import BaseModel
from datetime import date
from typing import List

class Genre(BaseModel):
    name: str
    genre_id: int

class Author(BaseModel):
    first_name: str
    last_name: str
    age: int

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int = None