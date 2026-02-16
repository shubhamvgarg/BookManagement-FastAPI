from pydantic import BaseModel

class BookCreate(BaseModel):
    id: int
    name: str
    author: str
    category: str
    cost: int

class BookResponse(BookCreate):
    pass
