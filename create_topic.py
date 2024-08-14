from confluent_kafka.admin import AdminClient, NewTopic

admin_client = AdminClient({'bootstrap.servers': 'localhost:19092'})


def example_create_topics(a: AdminClient = None, topics: list[str] = None) -> None:
    """
    Функция для создания топиков в Kafka

    :param a: AdminClient с параметрами инициализации. Default `None`.
    :param topics: Список топиков для создания. Default `None`.
    :return: Ничего не возвращает
    """

    new_topics = [NewTopic(topic, num_partitions=1, replication_factor=1) for topic in topics]
    # Call create_topics to asynchronously create topics, a dict
    # of <topic,future> is returned.
    fs = a.create_topics(new_topics)

    # Wait for operation to finish.
    # Timeouts are preferably controlled by passing request_timeout=15.0
    # to the create_topics() call.
    # All futures will finish at the same time.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} created".format(topic))
        except Exception as e:
            print("Failed to create topic {}: {}".format(topic, e))


example_create_topics(
    a=admin_client,
    topics=['test'],
)
