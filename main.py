from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet ():
    return("Welcome to the Server")

product = [
    Product(id=1,name="Apple",desc="Phone",price=12,quantity=2),
    Product(id=2,name="Samsung",desc="SmartPhone",price=124,quantity=5)


]
@app.get("/products")
def get_all_products ():
    return product
