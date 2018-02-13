import json

import arrow
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from flask import Flask, render_template, request
from forms import SignupForm, ChatForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat/send/<user>", methods=['POST'])
def chat_send(user):
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    form = ChatForm()
    user = user if user is not None else form.user.data
    future = producer.send(
        'pawk',
        {
            "username": user,
            "timestamp": arrow.utcnow().float_timestamp,
            "content": form.message.data
        })
    _ = future.get(timeout=1)

    return get(user)


@app.route("/send/<user>/<message>", methods=['GET'])
def send(user, message):
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    print(request.form)
    future = producer.send(
        'pawk',
        {
            "username": user,
            "timestamp": arrow.utcnow().float_timestamp,
            "content": message
        })
    _ = future.get(timeout=10)

    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        send(form.user.data, 'JOINED THE ROOM')
        return get(form.user.data)

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/get', methods=['GET'])
def get(user=None):
    form = ChatForm()

    if user is None:
        return signup()

    chats = []
    topic = 'pawk'
    consumer = KafkaConsumer(
        bootstrap_servers=['kafka:9092'],
        value_deserializer=json.loads)

    ps = [TopicPartition(topic, p) for p in consumer.partitions_for_topic(topic)]

    consumer.assign(ps)
    a = consumer.end_offsets(ps)
    offset = a[ps[0]]

    consumer.seek_to_beginning()

    for msg in consumer:
        msg.value['datetime'] = arrow.get(msg.value['timestamp']).humanize()
        chats.append(msg.value)
        if msg.offset >= offset - 1:
            consumer.close()
            break

    return render_template('chats.html', chats=chats, form=form, user=user)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
