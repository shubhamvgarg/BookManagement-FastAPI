from fastapi import FastAPI
from api.routes import book

app = FastAPI(
    title="Books Management",
    version="1.0.1"
)

app.include_router(book.router)
