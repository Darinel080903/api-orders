from abc import ABC
from typing import List
from domain.model.order_domain import Order_domain
from domain.model.order_product_domain import Order_products_domain
from domain.repository.order_repository import Order_repository
from domain.use_case.order_use_case import Order_use_case
from domain.model.status_enum import Status_enum


class Order_service(Order_use_case, ABC):
    def __init__(self, order_repository: Order_repository):
        self.order_repository = order_repository

    def add_order(self, order: Order_domain):
        new_order = self.order_repository.add_order(order)
        return new_order

    def add_order_product(self, order_id: str, order_products: List[Order_products_domain]):
        total_price = sum([product.price*product.quantity for product in order_products])
        self.order_repository.add_order_product(order_id, order_products)
        self.order_repository.update_total(order_id, total_price)
        return self.order_repository.get_by_id(order_id)

    def get_by_id(self, order_id: str) -> Order_domain:
        return self.order_repository.get_by_id(order_id)

    def update_status(self, order_id, status: Status_enum):
        self.order_repository.update_status(order_id, status)

    def get_order_products_by_id(self, order_id: str) -> List[Order_products_domain]:
        return self.order_repository.get_order_products_by_id(order_id)

    def get_all(self) -> List[Order_domain]:
        return self.order_repository.get_all()

    def update_total(self, order_id: str, price: int):
        self.order_repository.update_total(order_id, price)
