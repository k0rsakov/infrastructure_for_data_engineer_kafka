import json
import time
import random
from confluent_kafka import Producer

# Define the Kafka configuration
conf = {'bootstrap.servers': "localhost:19092"}

# Create a Producer instance with the above configuration
producer = Producer(conf)

while True:
    # Define some data to send to Kafka
    data = {
        "user_id": random.randint(1, 100),
        "first_name": "John",
        "message": f"Random Message {random.randint(1, 1000)}"
    }

    # Convert the data to a JSON string
    data_str = json.dumps(data)

    # Produce a message to the "test" topic
    producer.produce(topic="my_topic", value=data_str)

    # Flush the producer to ensure all messages are sent
    producer.flush()

    # Sleep for a second before producing the next set of messages
    time.sleep(3)
