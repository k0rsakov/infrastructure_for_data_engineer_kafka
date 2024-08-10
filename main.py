from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(**conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

for i in range(10):
    producer.produce('my_topic', key=str(i), value=f'message-{i}', callback=delivery_report)
    producer.poll(0)

producer.flush()