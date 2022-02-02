from fastapi import APIRouter, Depends

from src.gsheet import get_list_of_clients, list_of_sheets, get_training_list, get_payment_list, get_meals_plan
from src.routers.auth_router import User, get_current_active_user

router = APIRouter(
    prefix='/google-sheets'
)


@router.get('/clients')
def read_all_data():
    values = get_list_of_clients()
    return {"values": values}


@router.get('/training-list')
def training_list(current_user: User = Depends(get_current_active_user)):
    return get_training_list(title='{} {}'.format(current_user.id, current_user.name))


@router.get('/payments')
def payments(current_user: User = Depends(get_current_active_user)):
    return get_payment_list(title='{} {}'.format(current_user.id, current_user.name))


@router.get('/meals-plan')
def meal_plan(current_user: User = Depends(get_current_active_user)):
    return get_meals_plan(title='{} {}'.format(current_user.id, current_user.name))


@router.get('/sheets')
def sheets():
    # TODO: remove this route (it was used just in development phase)
    print('test 123')
    return list_of_sheets()
