# Aiven Demonstration
Welcome to my first attempt at using Aiven Services with Kafka and PostgreSQL! This is a pretty basic project that
simulates banking information being sent using a Kafka Producer, and consumed/stored in a PostgreSQL db on the Kafka Consumer side.

## Getting Started
The following are the requirements to be able to run this simulation:
1. Aiven Kafka and Aiven PostreSQL services must first be created. This can be done from the [Aiven Console](https://console.aiven.io/index.html).
2. Install the required python packages by running `pip install -r requirements.txt` in the root directory of this
project.
3. Set the following environment variables for your Kafka services. These can all be found in the "Overview" tab in the Aiven Kafka Service.
- KAFKA_HOST
- KAFKA_PORT

4. Download the Access Key, Access Certificate, and CA Certificate from the "Overview" tab in the Aiven Kafka Service. They **must** be placed in the `$HOME/aiven-ssl` directory, and **must** use the following naming convention:
- CA Certificate: `ca.pem`
- Access Certificate: `service.cert`
- Access Key: `service.key`

5. (Optional) Set the following environment variables if the optional PostgreSQL connection is desired. These can all be found in the "Overview" tab in the Aiven PostgreSQL Service.
- PG_USER
- PG_PASSWORD
- PG_HOST
- PG_PORT
- PG_DB_NAME



## Running Tests
Add info about how to run the test suite
