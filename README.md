# Mahsulotlar CRUD API (FastAPI)

FastAPI + SQLAlchemy 2.0 + SQLite asosidagi kichik CRUD loyiha.

## Tuzilma

```
fastapi_crud/
├── app/
│   ├── __init__.py
│   ├── database.py   # DB ulanish va sessiya
│   ├── models.py     # SQLAlchemy modeli (Product)
│   ├── schemas.py    # Pydantic sxemalari (validatsiya)
│   ├── crud.py       # DB bilan ishlash funksiyalari
│   └── main.py       # API endpointlar
├── requirements.txt
└── README.md
```

## Ishga tushirish

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

So'ng brauzerda oching: http://127.0.0.1:8000/docs (Swagger UI)

## Endpointlar

| Metod  | URL                     | Vazifasi                    |
|--------|-------------------------|-----------------------------|
| POST   | `/products`             | Yangi mahsulot qo'shish     |
| GET    | `/products`             | Ro'yxat (`skip`, `limit`, `search`) |
| GET    | `/products/{id}`        | Bitta mahsulot              |
| PUT    | `/products/{id}`        | To'liq yangilash            |
| PATCH  | `/products/{id}`        | Qisman yangilash            |
| DELETE | `/products/{id}`        | O'chirish                   |

## Misol so'rov

```bash
curl -X POST http://127.0.0.1:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Noutbuk", "description": "16GB RAM", "price": 7500000, "quantity": 5}'
```
