import sys
from typing import Optional
from fastapi import FastAPI

# import database
from routers import gsheet_router, register_router

app = FastAPI()

app.include_router(gsheet_router.router)
app.include_router(register_router.router)
#
# db = database.create_db_connection()

# db.put({"name": "alex", "age": 77})

# print(db)
# sys.stdout.flush()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# @app.get("/user")
# def user():
#     return db.fetch({"name": "alex"}).items[0]


