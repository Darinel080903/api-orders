from pydantic import BaseModel


class Order_products_entity(BaseModel):
    product_id: str
    price: int
    quantity: int
