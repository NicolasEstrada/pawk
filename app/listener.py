import sys
import json

from flask_socketio import emit, join_room, leave_room
from kafka import KafkaConsumer


def main():
    consumer = KafkaConsumer(
        'pawk',
        bootstrap_servers=['kafka:9092'],
        value_deserializer=json.loads)

    for msg in consumer:
        print(msg.topic, msg.value)
        emit('message', {"user":  msg.value['user'], "message": msg.value['message']})


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Closing app ...')
        sys.exit(0)
    except Exception as e:
        print('Unknown exception: {}'.format(e))
        sys.exit(1)
