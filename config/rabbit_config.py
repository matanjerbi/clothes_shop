import pika
import json
from typing import Any


class RabbitMQPublisher:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()

        # Declare queues
        self.channel.queue_declare(queue='update_inventory')
        self.channel.queue_declare(queue='save_purchase')
        self.channel.queue_declare(queue='create_shipping')
        self.channel.queue_declare(queue='send_email')

    def publish_message(self, queue_name: str, message: Any):
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(message)
        )

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()