from fastapi import APIRouter,status,HTTPException
from src.books.book_data import books
from src.books.schema import Book,BookUpdateModel
from typing import List



book_router = APIRouter()

@book_router.get("/",response_model=List[Book])
async def get_books_database():
    return books

@book_router.post('/',status_code=status.HTTP_200_OK)
async def create_book(book:Book):
    book_data = book.model_dump()
    books.append(book_data)
    return book_data

@book_router.get('/{book_id}')
async def get_book(book_id:int):
    for value in books:
        if value['id'] == book_id :
            return value
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="books not found")
    

@book_router.patch('/{book_id}')
async def update_book(book_id:int,book_data:BookUpdateModel):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_data.title
            book['author'] = book_data.author 
            book['page_count'] = book_data.page_count
            return book 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book id not found")
            
    

@book_router.delete('/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book id not found")