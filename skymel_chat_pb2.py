# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: skymel_chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11skymel_chat.proto\x12\x04node\"\xc8\x01\n\x07\x43ontact\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x11\n\twallet_id\x18\x02 \x01(\t\x12\x19\n\x11\x64isplay_image_url\x18\x03 \x01(\t\x12+\n#contact_added_utc_timestamp_nanosec\x18\x04 \x01(\x04\x12\x38\n0last_successful_interation_utc_timestamp_nanosec\x18\x05 \x01(\x04\x12\x12\n\nis_blocked\x18\x06 \x01(\x08\"\x92\x01\n\x17\x43ontactsListAndUserInfo\x12 \n\tuser_info\x18\x01 \x01(\x0b\x32\r.node.Contact\x12\x1f\n\x08\x63ontacts\x18\x02 \x03(\x0b\x32\r.node.Contact\x12\x34\n,contact_list_generated_utc_timestamp_nanosec\x18\x03 \x01(\x04\"P\n\nStoredData\x12\x42\n\x1b\x63ontacts_list_and_user_info\x18\x01 \x01(\x0b\x32\x1d.node.ContactsListAndUserInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'skymel_chat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONTACT._serialized_start=28
  _CONTACT._serialized_end=228
  _CONTACTSLISTANDUSERINFO._serialized_start=231
  _CONTACTSLISTANDUSERINFO._serialized_end=377
  _STOREDDATA._serialized_start=379
  _STOREDDATA._serialized_end=459
# @@protoc_insertion_point(module_scope)