from typing import Optional

from fastapi import FastAPI
from gsheet import read_all

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/read_all")
def read_all_data():
    values = read_all()
    return  { "values": values }

