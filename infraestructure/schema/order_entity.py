from typing import List
from pydantic import BaseModel
from datetime import datetime
from domain.model.status_enum import Status_enum
from domain.model.order_product_domain import Order_products_domain


class Order_entity(BaseModel):
    total: int
    status: Status_enum
