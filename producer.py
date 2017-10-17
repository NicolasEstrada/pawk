import sys
import json
import arrow

from kafka import KafkaProducer
from kafka.errors import KafkaError


def main():

    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    future = producer.send(
        'pawk',
        {
            "username": "nico",
            "timestamp": arrow.utcnow().float_timestamp,
            "content": "Hello channel"
        })
    _ = future.get(timeout=5)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Closing app ...')
        sys.exit(0)
    except KafkaError as e:
        print('Kafka error: {}'.format(e))
        sys.exit(1)
    except Exception as e:
        print('Unknown exception: {}'.format(e))
        sys.exit(2)
