import pika
import json


class RabbitMQ:
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=5672)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='order_updates')

    def publish_message(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key='order_updates',
            body=json.dumps(message)
        )
