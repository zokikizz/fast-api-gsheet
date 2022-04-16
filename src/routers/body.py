from pydantic import BaseModel


class CommentRequest(BaseModel):
    comment: str
    row: int
