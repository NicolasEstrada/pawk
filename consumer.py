import sys
import json

from kafka import KafkaConsumer


def main():
    consumer = KafkaConsumer(
        'pawk',
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='earliest',
        value_deserializer=json.loads)

    for msg in consumer:
        print(msg.topic, msg.value)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Closing app ...')
        sys.exit(0)
    except Exception as e:
        print('Unknown exception: {}'.format(e))
        sys.exit(1)
