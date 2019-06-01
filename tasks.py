from celery import Celery

from message_pb2 import MessageType1

app = Celery('example', broker='redis://localhost:6379/0')

@app.task
def process_message(enc):
    m = MessageType1()
    m.ParseFromString(enc.encode('utf-8'))
    print('got message:', m)
    return m
