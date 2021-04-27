# Aiven Demonstration
Welcome to my first attempt at using Aiven Services with Kafka and PostgreSQL! This is a pretty basic project that
simulates banking information being sent using a Kafka Producer, and consumed/stored in a PostgreSQL db on the Kafka
Consumer side

## Getting Started
The following are the requirements to be able to run this simulation:
1. Aiven Kafka and Aiven PostreSQL services must first be created. This can be done from the [Aiven Console](https://console.aiven.io/index.html)
2. Install the required python packages by running `pip install -r requirements.txt` in the root directory of this
project
3. Set the following environment variables if the optional PostgreSQL connection is desired:
- PG_USER
- PG_PASSWORD
- PG_HOST
- PG_PORT
- PG_DB_NAME
These can all be found in the "Overview" tab in the Aiven PostgreSQL Service. 

## Running Tests
Add info about how to run the test suite
