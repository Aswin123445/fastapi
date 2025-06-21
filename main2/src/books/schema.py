from pydantic import BaseModel


class BookUpdateModel(BaseModel):
    title:str
    author: str 
    page_count: int 

class Book(BaseModel):
    id:int
    title:str
    author: str 
    page_count: int