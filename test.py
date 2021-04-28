''' test.py
This file contains tests using the unittest framework
'''

import unittest
import os
from kafka_objects.producer import Producer
from kafka_objects.consumer import Consumer

class TestAccountOperations(unittest.TestCase):
    def setUp(self):
        # Initialize db connection
        db_config = {
            "user": os.getenv("PG_USER"),
            "password": os.getenv("PG_PASSWORD"),
            "host": os.getenv("PG_HOST"),
            "port": os.getenv("PG_PORT"),
            "db_name": os.getenv("PG_DB_NAME"),
        }

        # Initialize kafka producer and consumers
        kafka_host = os.getenv("KAFKA_HOST")
        kafka_port = os.getenv("KAFKA_PORT")
        self.producer = Producer(topic="demo-topic", host=kafka_host, \
                                 port=kafka_port)
        self.consumer = Consumer(topic="demo-topic", host=kafka_host, \
                                 port=kafka_port, db=db_config)

        # Delete any pre-existing rows from the bank_account table
        self.account = self.consumer.get_account_controller()
        query = ("DELETE FROM bank_account")
        self.account.run_query(query)

    def tearDown(self):
        query = ("DROP TABLE bank_account")
        self.account.run_query(query)
        self.producer.close_session()

    def test_single_account_creation(self):
        print("#### testing single account creation ####")

        # Simulate data production and consumption
        account_data = self.producer.produce_account_data()
        self.consumer.consume_account_data()

        # Check row count
        num_rows = self.account.get_table_size()
        self.assertEqual(num_rows, 1)

        # Check balance and firstname match
        rows = self.account.get_rows()
        self.assertEqual(rows[0]["firstname"], account_data["first"])
        self.assertEqual(str(rows[0]["accountbalance"]), account_data["balance"])

        print("#### single account creation: PASS####\n")

    def test_multiple_account_creation(self):
        print("#### testing multiple account creation ####")

        # Simulate data production and consumption
        account_data = []
        for i in range(10):
            account_data.append(self.producer.produce_account_data(i))
            self.consumer.consume_account_data()

        # Check row count
        num_rows = self.account.get_table_size()
        self.assertEqual(num_rows, 10)

        # Check balance and firstname match
        rows = self.account.get_rows()
        for idx, row in enumerate(rows):
            self.assertEqual(row["firstname"], account_data[idx]["first"])
            self.assertEqual(str(row["accountbalance"]), account_data[idx]["balance"])

        print("#### multiple account creation: PASS ####")
