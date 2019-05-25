.PHONY: protos
protos:
	protoc --proto_path=. --python_out=. message.proto

