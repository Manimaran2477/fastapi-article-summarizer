from pydantic import BaseModel, HttpUrl
from typing import Optional


class ArticleBase(BaseModel):
    title: Optional[str] = None


class ArticleCreate(BaseModel):
    source_url: HttpUrl


class ArticleUpdate(BaseModel):
    title: str


class ArticleResponse(BaseModel):
    id: str
    title: str
    content: str
    summary: str
    source_url: HttpUrl

    class Config:
        orm_mode = True
