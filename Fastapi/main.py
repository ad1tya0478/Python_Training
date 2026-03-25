from typing import Union
# typing - this is a standard python module used for type hints
from models import Product
import os
import tempfile
from fastapi import FastAPI
from pydantic import BaseModel  
# pydantic is used for data validation library for python

app = FastAPI()

#input schema 
class UserCreate(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users")
def create_item(user: UserCreate):
    return user

# output schema
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users/{id}", response_model=UserResponse)
def get_user(id: int):
    return {
        "id": id,
        "name": "Aditya",
        "email": "a@b.com",
        "password": "secret"
    }


@app.get("/")  # first end point, this is a decorator, it tells the fastapi that whenever someone sends a get req to /, run the function below..... get -> http method | / -> url path
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

products = [
    Product(id=1, name = "Phone", description = "Budget Phone", price = 99, quantity = 10),
    Product(id=2, name  = "Laptop", description = "Budget Lappy", price = 500, quantity = 15),
    Product(id=3, name="Victus", description="Gaming Laptop", price=900, quantity=8),
    Product(id=4, name="Omen", description="Gaming Laptop", price=1300, quantity=5),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for i in products:
        if i.id == id:
            return i
        
    return "Product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id:int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product addded succesfully"

    return "No product Found" 



