import json
import time
from confluent_kafka import Producer
from faker import Faker
import uuid_utils as uuid


def generate_list_of_dict() -> dict[str, str]:

    fake = Faker(locale='ru_RU')

    return {
        'uuid': str(uuid.uuid7()),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'middle_name': fake.middle_name(),
    }


# Define the Kafka configuration
conf = {'bootstrap.servers': "localhost:19092"}

# Create a Producer instance with the above configuration
producer = Producer(conf)


while True:
    # Define some data to send to Kafka
    data = generate_list_of_dict()

    # Convert the data to a JSON string
    data_str = json.dumps(data)

    # Produce a message to the "my_topic" topic
    producer.produce(topic="my_topic", value=data_str)

    # Flush the producer to ensure all messages are sent
    producer.flush()

    # Sleep for a second before producing the next set of messages
    time.sleep(3)
