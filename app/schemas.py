from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, examples=["Noutbuk"])
    description: str | None = Field(None, examples=["15.6 dyuymli, 16GB RAM"])
    price: float = Field(..., gt=0, examples=[7500000])
    quantity: int = Field(0, ge=0, examples=[10])


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    """Qisman yangilash (PATCH) — barcha maydonlar ixtiyoriy."""
    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = None
    price: float | None = Field(None, gt=0)
    quantity: int | None = Field(None, ge=0)


class ProductOut(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
