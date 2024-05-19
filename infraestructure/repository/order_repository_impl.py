from abc import ABC, abstractmethod
from typing import List

from domain.model.order_domain import Order_domain
from infraestructure.configuration.db import SessionLocal
from domain.repository.order_repository import Order_repository
from infraestructure.schema.models_factory import Orders, Order_product
from infraestructure.mappers.order_mapper import to_db_order, to_dict_order, to_domain_order, to_db_order_product, \
    to_domain_order_product
from domain.model.status_enum import Status_enum as OrderStatus
from domain.model.order_product_domain import Order_products_domain as OrderProductDomain


class Order_repository_impl(Order_repository, ABC):
    def __init__(self):
        self.db = SessionLocal()

    def add_order(self, order: Order_domain):
        db_order = to_db_order(order)
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        self.db.close()
        return to_dict_order(order)

    def update_status(self, order_id: str, status: OrderStatus):
        order = self.db.query(Orders).filter(Orders.id == order_id).first()
        order.status = OrderStatus(status)
        self.db.commit()
        self.db.refresh(order)
        self.db.close()

    def add_order_product(self, order_id: str, order_products: List[OrderProductDomain]):
        db_order_products = [to_db_order_product(product) for product in order_products]
        self.db.bulk_save_objects(db_order_products)
        self.db.commit()
        self.db.close()

    def update_total(self, order_id: str, price: int):
        order = self.db.query(Orders).filter(Orders.id == order_id).first()
        if order:
            order.total = price
            self.db.commit()
            self.db.refresh(order)
        self.db.close()

    def get_order_products_by_id(self, order_id: str) -> List[OrderProductDomain]:
        order_products = self.db.query(Order_product).filter(Order_product.order_id == order_id).all()
        return [to_domain_order_product(product, order_id) for product in order_products]

    def get_by_id(self, order_id: str) -> Order_domain:
        order = self.db.query(Orders).filter(Orders.id == order_id).first()
        return to_domain_order(order)

    def get_all(self) -> List[Order_domain]:
        return self.db.query(Orders).all()
