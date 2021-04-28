# Aiven Demonstration
Welcome to my first attempt at using Aiven Services with Kafka and PostgreSQL! This is a pretty basic project that
simulates banking information being sent using a Kafka Producer, and consumed/stored in a PostgreSQL db on the Kafka Consumer side.

## Getting Started
The following are the requirements to be able to run this simulation:
1. Aiven Kafka and Aiven PostreSQL services must first be created. This can be done from the [Aiven Console](https://console.aiven.io/index.html).
2. Install the required python packages by running `pip install -r requirements.txt` in the root directory of this
project.
3. Set the following environment variables for your Kafka services. These can all be found in the "Overview" tab in the Aiven Kafka Service.
- `export KAFKA_HOST="<your_kafka_hostname>"`
- `export KAFKA_PORT="<your_kafka_port>"`

4. Download the Access Key, Access Certificate, and CA Certificate from the "Overview" tab in the Aiven Kafka Service. They **must** be placed in the `$HOME/aiven-ssl/` directory, and **must** use the following naming convention:
- CA Certificate: `ca.pem`
- Access Certificate: `service.cert`
- Access Key: `service.key`

5. (Optional) Set the following environment variables if the optional PostgreSQL connection is desired. These can all be found in the "Overview" tab in the Aiven PostgreSQL Service.
- `export PG_USER="<your_postresql_username>"`
- `export PG_PASSWORD="<your_postresql_password>"`
- `export PG_HOST="<your_postresql_hostname>"`
- `export PG_PORT="<your_postresql_port>"`
- `export PG_DB_NAME="<your_postresql_db_name>"`

## Running Tests
The tests can be found in `test.py`. The unittest framework is used to run the tests with the following command in the root directory of this project:

`python -m unittest test`

The current test cases are integration tests that verify the producer->consumer->db pipeline.

## Contributing
A demo application can be found in `demo_app.py` to see the basic behaviour. This can be used as a starting point for adding more functionality and tests.

Some key next steps for this project are:
2. Expand the db's interface to run more complex queries (e.g. remove accounts, transfer funds, etc...)
3. More advanced message parsing on the consumer side to make use of the queries developed in (2.)
