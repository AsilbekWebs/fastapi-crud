from fastapi import FastAPI, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mahsulotlar CRUD API",
    description="FastAPI + SQLAlchemy + SQLite asosidagi kichik CRUD loyiha",
    version="1.0.0",
)


def get_or_404(product_id: int, db: Session) -> models.Product:
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Mahsulot topilmadi")
    return product


@app.get("/", tags=["root"])
def root():
    return {"message": "Mahsulotlar CRUD API ishlayapti. Hujjatlar: /docs"}


@app.post("/products", response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED, tags=["products"])
def create(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Yangi mahsulot qo'shish (Create)."""
    return crud.create_product(db, data)


@app.get("/products", response_model=list[schemas.ProductOut], tags=["products"])
def read_all(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    search: str | None = Query(None, description="Nom bo'yicha qidirish"),
    db: Session = Depends(get_db),
):
    """Barcha mahsulotlar ro'yxati (Read)."""
    return crud.get_products(db, skip, limit, search)


@app.get("/products/{product_id}", response_model=schemas.ProductOut, tags=["products"])
def read_one(product_id: int, db: Session = Depends(get_db)):
    """Bitta mahsulotni olish (Read)."""
    return get_or_404(product_id, db)


@app.put("/products/{product_id}", response_model=schemas.ProductOut, tags=["products"])
def replace(product_id: int, data: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Mahsulotni to'liq yangilash (Update)."""
    product = get_or_404(product_id, db)
    return crud.update_product(db, product, data, partial=False)


@app.patch("/products/{product_id}", response_model=schemas.ProductOut, tags=["products"])
def update(product_id: int, data: schemas.ProductUpdate, db: Session = Depends(get_db)):
    """Mahsulotni qisman yangilash (Update)."""
    product = get_or_404(product_id, db)
    return crud.update_product(db, product, data, partial=True)


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["products"])
def delete(product_id: int, db: Session = Depends(get_db)):
    """Mahsulotni o'chirish (Delete)."""
    product = get_or_404(product_id, db)
    crud.delete_product(db, product)
