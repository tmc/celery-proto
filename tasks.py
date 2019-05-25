from celery import Celery
from kombu.serialization import registry

# This import triggers population of the proto symbol database.
import message_pb2

# This injects a json encoding method for celery compatibility.
import proto_serialization
proto_serialization.attach_json_formatting(["message.proto"])

app = Celery('example', broker='redis://localhost:6379/0')

@app.task
def hello():
    return 'hello world'

@app.task
def process_message(m):
    print('got message:', m)
    return m
