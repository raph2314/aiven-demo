import time
import os
from kafka_objects.producer import Producer
from kafka_objects.consumer import Consumer

if __name__ == "__main__":
    db_config = {
        "user": os.getenv("PG_USER"),
        "password": os.getenv("PG_PASSWORD"),
        "host": os.getenv("PG_HOST"),
        "port": os.getenv("PG_PORT"),
        "db_name": os.getenv("PG_DB_NAME"),
    }

    # Initialize kafka objects
    kafka_host = os.getenv("KAFKA_HOST")
    kafka_port = os.getenv("KAFKA_PORT")
    producer = Producer(topic="demo-topic", host=kafka_host, port=kafka_port)
    consumer = Consumer(topic="demo-topic", host=kafka_host, port=kafka_port, \
                        db=db_config)

    # Simulate account data transfer
    for i in range(10):
        producer.produce_account_data(i)
        time.sleep(1)
        consumer.consume_account_data()

    # Synchronous call to ensure all messages are sent
    producer.close_session()
