from fastapi import APIRouter, HTTPException
from models.user_model import User
from db.db import connection

import os
import secrets
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from datetime import datetime
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

router = APIRouter(
    prefix='/api/register'
)

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME", None),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD", None),
    MAIL_FROM=os.getenv("MAIL_FROM", None),
    MAIL_PORT=os.getenv("MAIL_PORT", None),
    MAIL_SERVER=os.getenv("MAIL_SERVER", None),
    MAIL_FROM_NAME=os.getenv("MAIL_TITLE", None),
    MAIL_TLS=False,
    MAIL_SSL=True,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER='./templates/email'
)


def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        template_body=body,
        subtype='html',
    )
    fm = FastMail(conf)
    background_tasks.add_task(
        fm.send_message,
        message,
        template_name='email.html'
    )


@router.post("/")
def create_new_user(new_user: User, background_tasks: BackgroundTasks):

    users = connection.fetch({"email": new_user.Email_Address}).items

    if len(users) > 0:
        # if there is user with same email just return user that already exist
        raise HTTPException(409,
                            "User with email {} already exist.".format(new_user.Email_Address))

    user = {
        "email": new_user.Email_Address,
        "password": "",
        "activated": False,
        "activation_token": ''.join([secrets.choice('1234567890') for i in range(6)]),
        "authorization_token": "",
        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    connection.put(user)

    send_email_background(
        background_tasks=background_tasks,
        subject="Activate your account",
        email_to=user["email"],
        body={
            "title": "Activate your account with following token",
            "token": user["activation_token"],
            "paragraph": "Enter this token on first opening of the application to set up password for your account.",
            "button": None
        }
    )

    return JSONResponse(content=jsonable_encoder(user))
