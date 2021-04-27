from postgresql import db
from kafka import KafkaConsumer
from psycopg2 import DatabaseError
import json
import os

class Consumer():
    '''
    Kafka Consumer based on "Getting Started with Aiven for Apache Kafka"
    https://help.aiven.io/en/articles/489572-getting-started-with-aiven-for-apache-kafka
    '''

    def __init__(self, topic, host, port, **kwargs):
        self.consumer = KafkaConsumer(
            topic,
            auto_offset_reset="earliest",
            bootstrap_servers="{}:{}".format(host, port),
            client_id="demo-client-1",
            group_id="demo-group",
            security_protocol="SSL",
            ssl_cafile=os.getenv("HOME") + "/aiven-ssl/ca.pem",
            ssl_certfile=os.getenv("HOME") + "/aiven-ssl/service.cert",
            ssl_keyfile=os.getenv("HOME") + "/aiven-ssl/service.key",
        )

        # Instantiate db and create table if necessary
        self.db_configured = False
        db_config = kwargs["db"]
        try:
            uri = "postgres://{user}:{pwd}@{host}:{port}/{db_name}?sslmode=require" \
                  .format(user=db_config["user"], pwd=db_config["password"], \
                          host=db_config["host"], port=db_config["port"], \
                          db_name=db_config["db_name"])
            self.account = db.AccountsController(uri)
            self.account.create_table()
            self.db_configured = True
            print("Consumer configured with postgresql")

        except KeyError as key_err:
            print("Failed to initialize db. Invalid db credential key: ", key_err)
        except DatabaseError as db_err:
            print("Unable to initialize db:\n", db_err)

    def consume_account_data(self):
        for _ in range(2):
            raw_msgs = self.consumer.poll(timeout_ms=1000)
            for tp, msgs in raw_msgs.items():
                for msg in msgs:
                    account = json.loads(msg.value.decode("utf-8").replace("\'", "\""))

                    # Only store if db is configured
                    if self.db_configured:
                        self.account.add_account(account)

        self.consumer.commit()
