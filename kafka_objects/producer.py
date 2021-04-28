from kafka import KafkaProducer
from faker import Faker
import random
import json
import os

class Producer():
    '''
    Kafka Producer based on "Getting Started with Aiven for Apache Kafka"
    https://help.aiven.io/en/articles/489572-getting-started-with-aiven-for-apache-kafka
    '''
    def __init__(self, topic, host, port):
        self.topic = topic
        self.fake = Faker()
        self.producer = KafkaProducer(
            bootstrap_servers="{}:{}".format(host, port),
            security_protocol="SSL",
            ssl_cafile=os.getenv("HOME") + "/aiven-ssl/ca.pem",
            ssl_certfile=os.getenv("HOME") + "/aiven-ssl/service.cert",
            ssl_keyfile=os.getenv("HOME") + "/aiven-ssl/service.key",
        )

    def produce_account_data(self, iter=0):
        # Simulate account data
        account_data = {
            "first": self.fake.first_name(),
            "last": self.fake.last_name(),
            "address": self.fake.address().replace("\n", " "),
            "balance": self.fake.pricetag()[1:].replace(",", ""),
            "account_type": "chequings" if random.uniform(0,1) > 0.5 else "savings",
        }
        print("KAFKA PRODUCER: account produced for", account_data["first"])
        self.producer.send(self.topic, json.dumps(account_data).encode("utf-8"))
        return account_data

    def close_session(self):
        self.producer.flush()
