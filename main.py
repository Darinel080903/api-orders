import json
import pika
from fastapi import FastAPI

from infraestructure.configuration.rabbit_connection import RabbitMQ
from infraestructure.web.rest.controller import routes
import uvicorn

app = FastAPI()

rabbitmq = RabbitMQ()

app.include_router(routes.controller)

if __name__ == "__main__":
    uvicorn.run(app, port=3001)
