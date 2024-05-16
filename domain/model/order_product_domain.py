from uuid import uuid4


class Order_products_domain:
    def __init__(self, order_id: str, product_id: str, price: int, quantity: int):
        self.id = str(uuid4())
        self.order_id = order_id
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def get_id(self):
        return self.id

    def get_product_id(self):
        return self.product_id

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity
