from fastapi import APIRouter, HTTPException
from schemas.book import BookCreate
from services import book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/")
def get_books():
    return book_service.get_all_books()

@router.get("/{book_id}")
def get_book(book_id: int):
    book = book_service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/")
def create_book(book: BookCreate):
    return book_service.add_book(book)

@router.put("/{book_id}")
def update_book(book_id: int, book: BookCreate):
    updated = book_service.update_book(book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}")
def delete_book(book_id: int):
    deleted = book_service.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted
