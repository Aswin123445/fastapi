from fastapi import FastAPI,HTTPException
from typing import Optional,List
from enum import IntEnum
from pydantic import BaseModel,Field
app = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2 
    HIGH = 1 

#parent class
class BaseTodo(BaseModel):
    todo_name :str = Field(...,min_length=4,max_length=256,description="name of the todo")
    todo_description :str = Field(...,min_length=10,max_length=300,description="what this todo have to do")
    priority : Priority = Field(default=Priority.LOW,description="set the priority of the todo")


class TodoCreate(BaseTodo):
    pass 

class Todo(BaseTodo):
    todo_id :int = Field(...,description="unique identifier of the todo ")

class UpdateTodo(BaseModel):
    todo_name :Optional[str] = Field(None,min_length=4,max_length=256,description="name of the todo")
    todo_description :Optional[str] = Field(None,min_length=10,max_length=300,description="what this todo have to do")
    priority : Optional[Priority] = Field(None,description="set the priority of the todo")

todo_list = [
    Todo(todo_id=1,todo_name='Sports',todo_description='i have to go to gym tomorror',priority=1),
    Todo(todo_id=1,todo_name='Meeting',todo_description='Meeting for morning',priority=2),
    Todo(todo_id=1,todo_name='Sports',todo_description='i have to go to gym tomorror',priority=1),
]


@app.get("/todos",response_model=Todo)
def get_todo(id :int = None):
    for todo in todo_list:
        if todo.todo_id == id:
            return todo
    raise HTTPException(404,'please add the id to access data')
    
        
@app.get("/todos",response_model=List[Todo])
def todos():
    return todo_list

    
@app.post('/add_todo',response_model=Todo)
def add_todo(data:TodoCreate):
    id = max(i.todo_id for i in todo_list) + 1 
    
    new_data = Todo(todo_id=id,todo_name=data.todo_name,todo_description = data.todo_description)
    todo_list.append(new_data)
    return new_data

@app.put('/update_todo',response_model=Todo)
def update_todo(id: int,updated_todo = UpdateTodo):
    for data in todo_list:
        if id == data.todo_id:
            data.todo_name = 'Tour'
            data.todo_description = update_todo.todo_description
            data.priority = update_todo.priority
            return data
        
@app.delete('/delete',response_model=Todo)
def delete_todo(id:int):
    for index,data in enumerate(todo_list):
        if id == data.todo_id:
            return data.pop(index)
    
    

    
        