from fastapi import FastAPI 
from src.books.router import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print('server is started')
    await init_db()
    yield
    print('server is ended')

version = "v1"
app = FastAPI(
    version=version,
    lifespan=life_span
)
app.include_router(book_router,prefix=f'/api/{version}/books',tags=['books'])