from sqlalchemy.orm import Session
from app.models import Article


def create_article(db: Session, article: Article):
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_article(db: Session, article_id: str):
    return db.query(Article).filter(Article.id == article_id).first()


def delete_article(db: Session, article: Article):
    db.delete(article)
    db.commit()
