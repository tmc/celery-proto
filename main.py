import base64
from tasks import hello
from message_pb2 import MessageType1
from tasks import process_message

#hello.apply_async()

m = MessageType1(name="hello")

process_message.apply_async([m])
#process_message.apply_async([m], serializer='protobuf')
