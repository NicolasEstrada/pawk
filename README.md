# pawk
Playing Around With Kafka


## Dependencies

https://hub.docker.com/r/wurstmeister/kafka/

## Building and deployment

The *pawk* project has its own Dockerfile to be built and deployed using any container manager that is compatible with it.
To create the docker image, just run within `pawk/` folder the following:

```bash
docker build -t pawk .
```

In order to run the app, do the following:

```bash
docker run -d pawk 
```

To login the docker container using a bash console:

```bash
docker exec -i -t CONTAINER_ID /bin/bash
```

To compose services:

```bash
docker-compose up -d
docker-compose ps
docker-compose stop
// to stop the application
docker-compose down
```

To get docker app ip:

```bash
docker-machine ip MACHINE_VM
```

For local testing, you need to add the following entry in `/etc/hosts`:

```bash
127.0.0.1       localhost kafka
```

### Extra Info

https://wurstmeister.github.io/kafka-docker/
https://docs.docker.com/compose/gettingstarted/#step-4-build-and-run-your-app-with-compose
https://stackoverflow.com/questions/35861501/kafka-in-docker-not-working
https://hub.docker.com/r/wurstmeister/kafka/
https://github.com/PrettyPrinted/flask-socketio-chat/blob/master/main.py
https://github.com/miguelgrinberg/Flask-SocketIO-Chat/blob/master/app/main/events.py
