from abc import ABC, abstractmethod
from typing import List
from domain.model.order_domain import Order_domain
from domain.model.order_product_domain import Order_products_domain
from domain.model.status_enum import Status_enum
from domain.repository.order_repository import Order_repository


class Order_use_case(ABC):

    @abstractmethod
    def __init__(self, order_repository: Order_repository):
        self.order_repository = order_repository

    @abstractmethod
    def add_order(self, order: Order_domain):
        raise NotImplemented

    @abstractmethod
    def update_status(self, order_id: str, status: str):
        raise NotImplemented

    @abstractmethod
    def add_order_product(self, order_id: str, order_product: List[Order_products_domain]):
        raise NotImplemented

    @abstractmethod
    def get_order_products_by_id(self, order_id: str) -> List[Order_products_domain]:
        raise NotImplemented

    @abstractmethod
    def update_total(self, order_id: str, price: int):
        raise NotImplemented

    @abstractmethod
    def get_by_id(self, order_id: str) -> Order_domain:
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> List[Order_domain]:
        raise NotImplemented
