from fastapi import FastAPI 
from src.books.router import book_router

version = "v1"
app = FastAPI(
    version=version
)
app.include_router(book_router,prefix=f'/api/{version}/books',tags=['books'])