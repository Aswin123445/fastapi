from pydantic import BaseModel
import uuid
from datetime import datetime

class BookUpdateModel(BaseModel):
    title:str
    author: str 
    publisher:str
    language:str
    page_count: int 

class Book(BaseModel):
    uid:uuid.UUID
    title:str
    publisher:str
    author: str 
    published_date:str
    page_count: int
    language:str
    created_at:datetime
    updated_at:datetime
    
class BookCreateModel(BaseModel):
    title:str
    author: str 
    publisher:str
    language:str
    page_count: int
    published_date:str
  