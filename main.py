import sys
from typing import Optional
from fastapi import FastAPI, Request, Response

# import database
from routers import gsheet_router, register_router
from db.db import connection

app = FastAPI()

app.include_router(gsheet_router.router)
app.include_router(register_router.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = connection
        response = await call_next(request)
    except Exception as e:
        print("Error: ", str(e))

    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



