from fastapi import Request


def get_db_connection(request: Request):
    return request.state.db