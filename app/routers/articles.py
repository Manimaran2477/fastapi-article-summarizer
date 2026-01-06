
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import ArticleCreate, ArticleUpdate, ArticleResponse
from app.models import Article
from app.services.external_api import fetch_article
from app import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/articles", response_model=ArticleResponse, status_code=201)
async def create_article(payload: ArticleCreate, db: Session = Depends(get_db)):
    data = await fetch_article(str(payload.source_url))
    article = Article(
        title=data.get("title", "Untitled"),
        content=data.get("body", ""),
        summary=data.get("body", "")[:100],
        source_url=str(payload.source_url)
    )
    return crud.create_article(db, article)

@router.get("/articles/{article_id}", response_model=ArticleResponse)
def get_article(article_id: str, db: Session = Depends(get_db)):
    article = crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.put("/articles/{article_id}", response_model=ArticleResponse)
def update_article(article_id: str, payload: ArticleUpdate, db: Session = Depends(get_db)):
    article = crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404)
    article.title = payload.title
    db.commit()
    return article

@router.delete("/articles/{article_id}", status_code=204)
def delete_article(article_id: str, db: Session = Depends(get_db)):
    article = crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404)
    crud.delete_article(db, article)
