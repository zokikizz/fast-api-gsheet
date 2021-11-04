from fastapi import APIRouter

from gsheet import read_all

router = APIRouter(
    prefix="/api/gsheet"
)


@router.get("/read_all")
def read_all_data():
    values = read_all()
    return {"values": values}
