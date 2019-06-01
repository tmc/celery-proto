from message_pb2 import MessageType1
from tasks import process_message

m = MessageType1(name="hello")

s = m.SerializeToString().decode('utf-8')
process_message.apply_async([s])
