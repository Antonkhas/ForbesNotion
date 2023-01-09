from pydantic import BaseModel
from datetime import date


class Book(BaseModel):
    title: str
    writer: str
    date: date
    duration: str
    pages: int
    genres: str = None


# отправляем данные на наш сервер