from domain.model.order_domain import Order_domain
from domain.model.order_product_domain import Order_products_domain
from infraestructure.schema.models_factory import Orders
from infraestructure.schema.models_factory import Order_product
from infraestructure.schema.order_products_entity import Order_products_entity


def to_domain_order(db_order: Orders) -> Order_domain:
    return Order_domain(
        total=db_order.total,
        status=db_order.status
    )


def to_db_order(domain_order: Order_domain) -> Orders:
    return Orders(
        id=domain_order.get_id(),
        total=domain_order.get_total(),
        date=domain_order.get_date(),
        status=domain_order.get_status()
    )


def to_domain_order_product(db_order_product: Order_products_entity, order_id:str) -> Order_products_domain:
    return Order_products_domain(
        order_id=order_id,
        product_id=db_order_product.product_id,
        price=db_order_product.price,
        quantity=db_order_product.quantity
    )


def to_db_order_product(domain_order_product: Order_products_domain) -> Order_product:
    return Order_product(
        id=domain_order_product.get_id(),
        order_id=domain_order_product.order_id,
        product_id=domain_order_product.product_id,
        price=domain_order_product.price,
        quantity=domain_order_product.quantity
    )


def to_dict_order(domain_order: Order_domain) -> dict:
    return {
        "id": domain_order.get_id(),
        "total": domain_order.get_total(),
        "date": domain_order.get_date(),
        "status": domain_order.get_status()
    }
