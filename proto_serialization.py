# This file defines a helper that attaches json formatting methods to protobuf message types.
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import json_format

def attach_json_formatting(proto_file_names):
    """
    Attaches __json__ methods to the types defined in the provided proto file names.
    """
    _sym_db = _symbol_database.Default()
    for cls in _sym_db.GetMessages(proto_file_names).values():
      cls.__json__ = lambda x: json_format.MessageToJson(x,True)
