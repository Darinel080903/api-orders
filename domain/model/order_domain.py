from datetime import datetime
from uuid import uuid4

from domain.model.order_product_domain import Order_products_domain
from domain.model.status_enum import Status_enum


class Order_domain:
    def __init__(self, total: int, status: Status_enum):
        self.id = str(uuid4())
        self.total = total
        self.date = datetime.now()
        self.status = status

    def get_id(self):
        return self.id

    def get_total(self):
        return self.total

    def get_date(self):
        return self.date

    def get_status(self):
        return self.status

    def set_total(self, total):
        self.total = total

    def set_date(self, date):
        self.date = date

    def set_status(self, status):
        self.status = status
