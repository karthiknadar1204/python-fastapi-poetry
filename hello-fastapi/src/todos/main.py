from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get("/")
def root():
    return "Hello World"

@app.get("/gettodos/{id}")
def get_todos(id:int):
    print("get todos")
    return f"get todos called {id}"

@app.get("/getSingleTodo")
def getSingleTodo():
    print("get single todo")
    return "get single todo called"


def start():
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8080, reload=True)