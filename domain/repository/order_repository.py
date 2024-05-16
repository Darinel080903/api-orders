from typing import List
from abc import ABC, abstractmethod
from domain.model.order_domain import Order_domain
from domain.model.status_enum import Status_enum
from domain.model.order_product_domain import Order_products_domain


class Order_repository(ABC):
    @abstractmethod
    def add_order(self, order: Order_domain):
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> List[Order_domain]:
        raise NotImplemented

    @abstractmethod
    def add_order_product(self, order_id: str, order_product: List[Order_products_domain]):
        raise NotImplemented

    @abstractmethod
    def update_total(self, order_id: str, price: int):
        raise NotImplemented

    @abstractmethod
    def get_by_id(self, order_id: str) -> Order_domain:
        raise NotImplemented

    @abstractmethod
    def update_status(self, order_id: str, status: Status_enum):
        raise NotImplemented
