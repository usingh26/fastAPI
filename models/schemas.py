from pydantic import BaseModel
from typing import List

class Category(BaseModel):
    id: int 
    name: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool
    tags: List[str] = []
    category: Category
