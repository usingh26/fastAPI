from fastapi import APIRouter
from models.schemas import Product
from models.schemas import Category

router = APIRouter(prefix="/products")


products = [
    Product(
        id= 1,
        name="Laptop",
        price=75000.0,
        in_stock=True,
        tags=["electronics", "computer"],
        category=Category(id=1, name="Electronics")
    ),
    Product(
        id = 2,
        name="Phone",
        price=55000.0,
        in_stock=True,
        tags=["electronics", "Mobile"],
        category=Category(id=1, name="Electronics")
    ),
    Product(
        id = 3,
        name="Book",
        price=300.0,
        in_stock=False,
        tags=["education"],
        category=Category(id=2, name="Books")
    )
]



@router.get("/")
def get_products():
    return products

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):

    for product in products:
        if(product.id == product_id):
            return product
    return {"error" : "Product not found"} 
# here if i retrun error in this format then it gives me internal server error
# because pydantic expect response as in Product format here
