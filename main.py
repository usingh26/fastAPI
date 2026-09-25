
from fastapi import FastAPI
from routers.products import router as product_router
from routers.category import router as category_router

app = FastAPI()

app.include_router(product_router)
app.include_router(category_router)