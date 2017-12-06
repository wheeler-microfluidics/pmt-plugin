# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='mr_box_peripheral_board',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x63onfig.proto\x12\x17mr_box_peripheral_board\"\x9a\x01\n\x06\x43onfig\x12\x0c\n\x02id\x18\x04 \x01(\t:\x00\x12\x1f\n\x14zstage_down_position\x18\x32 \x01(\x02:\x01\x30\x12 \n\x12zstage_up_position\x18\x33 \x01(\x02:\x04\x31\x30.1\x12!\n\x13pmt_control_voltage\x18\x34 \x01(\r:\x04\x31\x30\x30\x30\x12\x1c\n\x11pmt_sampling_rate\x18\x35 \x01(\r:\x01\x31')
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='mr_box_peripheral_board.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mr_box_peripheral_board.Config.id', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pmt_control_voltage', full_name='mr_box_peripheral_board.Config.pmt_control_voltage', index=3,
      number=52, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pmt_sampling_rate', full_name='mr_box_peripheral_board.Config.pmt_sampling_rate', index=4,
      number=53, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:mr_box_peripheral_board.Config)
  ))
_sym_db.RegisterMessage(Config)


# @@protoc_insertion_point(module_scope)