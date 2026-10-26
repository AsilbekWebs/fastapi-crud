from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 100, search: str | None = None):
    stmt = select(models.Product)
    if search:
        stmt = stmt.where(models.Product.name.ilike(f"%{search}%"))
    stmt = stmt.order_by(models.Product.id).offset(skip).limit(limit)
    return db.scalars(stmt).all()


def get_product(db: Session, product_id: int):
    return db.get(models.Product, product_id)


def create_product(db: Session, data: schemas.ProductCreate):
    product = models.Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product: models.Product, data: schemas.ProductUpdate | schemas.ProductCreate, partial: bool):
    for field, value in data.model_dump(exclude_unset=partial).items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product: models.Product):
    db.delete(product)
    db.commit()
