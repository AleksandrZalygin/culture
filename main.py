from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items")
def get_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def get_items(item_id):
    return {"item": ["item1", "item2", "item3"][item_id]}