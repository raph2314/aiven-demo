from kafka import KafkaProducer
from faker import Faker
import random
import json

class Producer():
    def __init__(self, topic, host, port):
        self.fake = Faker()
        self.producer = KafkaProducer(
            bootstrap_servers="{}:{}".format(host, port),
            security_protocol="SSL",
            ssl_cafile="ssl/ca.pem",
            ssl_certfile="ssl/service.cert",
            ssl_keyfile="ssl/service.key",
        )

        self.topic = topic

    def produce_account_data(self, iter):
        account_data = {
            "first": self.fake.first_name(),
            "last": self.fake.last_name(),
            "address": self.fake.address().replace("\n", " "),
            "balance": self.fake.pricetag()[1:].replace(",", ""),
            "account_type": "chequings" if random.uniform(0,1) > 0.5 else "savings",
        }

        print("Sending {}: {}".format(iter, account_data))
        self.producer.send(self.topic, json.dumps(account_data).encode("utf-8"))

    def close_session(self):
        self.producer.flush()
