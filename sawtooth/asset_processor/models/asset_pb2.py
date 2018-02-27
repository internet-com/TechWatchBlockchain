# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: models/asset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from models import rule_pb2 as models_dot_rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='models/asset.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12models/asset.proto\x1a\x11models/rule.proto\"r\n\x05\x41sset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tnum_steps\x18\x04 \x01(\r\x12\x11\n\tcurr_step\x18\x05 \x01(\r\x12\x14\n\x05rules\x18\x06 \x03(\x0b\x32\x05.Rule\")\n\x0e\x41ssetContainer\x12\x17\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x06.Assetb\x06proto3')
  ,
  dependencies=[models_dot_rule__pb2.DESCRIPTOR,])




_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Asset.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Asset.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='Asset.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_steps', full_name='Asset.num_steps', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curr_step', full_name='Asset.curr_step', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rules', full_name='Asset.rules', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=155,
)


_ASSETCONTAINER = _descriptor.Descriptor(
  name='AssetContainer',
  full_name='AssetContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='AssetContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=198,
)

_ASSET.fields_by_name['rules'].message_type = models_dot_rule__pb2._RULE
_ASSETCONTAINER.fields_by_name['entries'].message_type = _ASSET
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['AssetContainer'] = _ASSETCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), dict(
  DESCRIPTOR = _ASSET,
  __module__ = 'models.asset_pb2'
  # @@protoc_insertion_point(class_scope:Asset)
  ))
_sym_db.RegisterMessage(Asset)

AssetContainer = _reflection.GeneratedProtocolMessageType('AssetContainer', (_message.Message,), dict(
  DESCRIPTOR = _ASSETCONTAINER,
  __module__ = 'models.asset_pb2'
  # @@protoc_insertion_point(class_scope:AssetContainer)
  ))
_sym_db.RegisterMessage(AssetContainer)


# @@protoc_insertion_point(module_scope)
