from typing import List

from fastapi import APIRouter

from infraestructure.configuration.rabbit_connection import RabbitMQ
from infraestructure.repository import order_repository_impl
from application.service.order_service import Order_service
from domain.model.order_domain import Order_domain
from infraestructure.schema.order_products_entity import Order_products_entity
from infraestructure.web.dto.response.base_response import Base_response
from domain.model.status_enum import Status_enum
from infraestructure.mappers.order_mapper import to_domain_order_product


controller = APIRouter()
repository = order_repository_impl.Order_repository_impl()
service = Order_service(repository)
rabbit = RabbitMQ()


@controller.get("/")
def get_orders():
    orders = service.get_all()
    return [order.__dict__ for order in orders]


@controller.post("/create", response_model=Base_response)
def create_order(order: List[Order_products_entity]):
    domain_order = Order_domain(total=0, status=Status_enum.CREATED)
    order_save = service.add_order(domain_order)
    domain_order_products = [to_domain_order_product(product, order_save['id']) for product in order]
    order_save = service.add_order_product(order_save['id'], domain_order_products)
    return Base_response(data=order_save.__dict__, message="Order created successfully")


@controller.put("/update/{order_id}/{status}", response_model=Base_response)
def update_order_status(order_id: str, status: Status_enum):
    service.update_status(order_id, status)
    if status == Status_enum.SEND:
        order_products = service.get_order_products_by_id(order_id)
        order_products_dicts = [product.__dict__ for product in order_products]
        message = {"products": order_products_dicts}
        rabbit.publish_message(message)
    return Base_response(data=None, message="Order status updated successfully")
