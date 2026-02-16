from typing import List
from schemas.book import BookCreate

books: List[BookCreate] = []

def get_all_books():
    return books

def get_book_by_id(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return None

def add_book(book: BookCreate):
    books.append(book)
    return book

def update_book(book_id: int, updated_book: BookCreate):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return updated_book
    return None

def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            return books.pop(i)
    return None
