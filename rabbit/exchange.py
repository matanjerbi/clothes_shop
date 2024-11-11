import pika
import json


def publish_to_queue(queue_name: str, message: dict):
    """פונקציה פשוטה לשליחת הודעה לתור"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # יצירת התור אם הוא לא קיים
    channel.queue_declare(queue=queue_name)

    # שליחת ההודעה
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(message)
    )

    connection.close()