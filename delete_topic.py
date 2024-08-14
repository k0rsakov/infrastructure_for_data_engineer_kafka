from confluent_kafka.admin import AdminClient

admin_client = AdminClient({'bootstrap.servers': 'localhost:19092'})


def example_delete_topics(a: AdminClient = None, topics: list[str] = None) -> None:
    """
    Функция для удаления топиков в Kafka.

    :param a: AdminClient с параметрами инициализации. Default `None`.
    :param topics: Список топиков для удаления. Default `None`.
    :return: Ничего не возвращает.
    """

    fs = a.delete_topics(topics, operation_timeout=30)

    # Wait for operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} deleted".format(topic))
        except Exception as e:
            print("Failed to delete topic {}: {}".format(topic, e))


example_delete_topics(
    a=admin_client,
    topics=['test'],
)