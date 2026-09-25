from fastapi import APIRouter
from models.schemas import Category
from typing import List

router = APIRouter(prefix="/categories")

categories = [
    Category(
        id=1,
        name="electronics"
    ),
    Category(
            id=2,
            name="books"
        ),
    Category(
                id=1,
                name="phones"
            )
]

@router.get("/", response_model=List[Category])
def get_category():
    return categories