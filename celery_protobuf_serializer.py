from kombu.serialization import registry

def enc(payload):
    return payload[0][0].SerializeToString()

def dec(payload, *args,**kwargs):
    ret = MessageType1()
    ret.ParseFromString(payload)
    return [[ret], dict(), None]

registry.register(
    'protobuf',
    encoder = enc,
    decoder = dec,
    content_type = 'application/x-protobuf',
    #content_encoding = 'binary',
)
