from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from typing import Optional,List
from pydantic import BaseModel


books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English"
    },
    {
        "id": 2,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2020-07-15",
        "page_count": 790,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Effective Python",
        "author": "Brett Slatkin",
        "publisher": "Pearson Education",
        "published_date": "2022-03-22",
        "page_count": 320,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Automate the Boring Stuff",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2015-11-20",
        "page_count": 504,
        "language": "English"
    }
]

class BookUpdateModel(BaseModel):
    title:str
    author: str 
    page_count: int 

class Book(BaseModel):
    id:int
    title:str
    author: str 
    page_count: int

app = FastAPI()

@app.get('/books',response_model=List[Book])
async def get_books_database():
    return books

@app.post('/book',status_code=status.HTTP_200_OK)
async def create_book(book:Book):
    book_data = book.model_dump()
    books.append(book_data)
    return book_data

@app.get('/book/{book_id}')
async def get_book(book_id:int):
    for value in books:
        if value['id'] == book_id :
            return value
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="books not found")
    

@app.patch('/book/{book_id}')
async def update_book(book_id:int,book_data:BookUpdateModel):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_data.title
            book['author'] = book_data.author 
            book['page_count'] = book_data.page_count
            return book 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book id not found")
            
    

@app.delete('/book/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book id not found")







# @app.get('/')
# async def input_helo():
#     return {'message':'helo world'}


# @app.get('/who_are_you/{name}')
# async def who(name:str):
#     return {'message':f'i am {name}'}

# @app.get('/bill')
# async def data(price:int,gst:str,invoice:Optional[str] = '0000000') -> dict:
#     return {
#         'price':price,
#         'gst':gst,
#         'invoice':invoice
#     }
    
    
# class Book(BaseModel):
#     title:str 
#     audher:str 
#     price:int 
#     pages:int 
#     rating:int  
    
# @app.post('/book_info')
# async def books_info(book:Book):
#     return {
#         'name':book.title,
#         'audher':book.audher,
#         'price':book.price
#     }
    
