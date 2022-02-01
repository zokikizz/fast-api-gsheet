from fastapi import APIRouter

from gsheet import get_list_of_clients

router = APIRouter(
    prefix='/google-sheets'
)


@router.get('/clients')
def read_all_data():
    values = get_list_of_clients()
    return {"values": values}


@router.get('/training-list')
def training_list():
    return []
