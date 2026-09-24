from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Category(BaseModel):
    id: int 
    name: str

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool
    tags: List[str] = []
    category: Category


products = [
    Product(
        name="Laptop",
        price=75000.0,
        in_stock=True,
        tags=["electronics", "computer"],
        category=Category(id=1, name="Electronics")
    ),
    Product(
        name="Phone",
        price=55000.0,
        in_stock=True,
        tags=["electronics", "Mobile"],
        category=Category(id=1, name="Electronics")
    ),
    Product(
        name="Book",
        price=300.0,
        in_stock=False,
        tags=["education"],
        category=Category(id=2, name="Books")
    )
]

@app.get("/products", response_model=List[Product])
def get_products():
    return products

@app.post("/products", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product


