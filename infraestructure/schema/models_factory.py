from sqlalchemy import String, Column, Table, Integer, ForeignKey, DateTime, Enum
from infraestructure.configuration.db import Base, engine, meta
from sqlalchemy.orm import relationship
from domain.model.status_enum import Status_enum


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(String(255), primary_key=True, unique=True)
    total = Column(Integer)
    date = Column(DateTime)
    status = Column(Enum(Status_enum))

    order_product = relationship("Order_product", back_populates="orders")


class Order_product(Base):
    __tablename__ = 'orders_products'
    id = Column(String(255), primary_key=True, unique=True)
    order_id = Column(String(255), ForeignKey('orders.id'))
    product_id = Column(String(255))
    price = Column(Integer)
    quantity = Column(Integer)

    orders = relationship("Orders", back_populates="order_product")


Base.metadata.create_all(engine)
