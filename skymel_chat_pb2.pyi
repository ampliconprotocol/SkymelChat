from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contact(_message.Message):
    __slots__ = ["contact_added_utc_timestamp_nanosec", "display_image_url", "display_name", "is_blocked", "last_successful_interation_utc_timestamp_nanosec", "wallet_id"]
    CONTACT_ADDED_UTC_TIMESTAMP_NANOSEC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_INTERATION_UTC_TIMESTAMP_NANOSEC_FIELD_NUMBER: _ClassVar[int]
    WALLET_ID_FIELD_NUMBER: _ClassVar[int]
    contact_added_utc_timestamp_nanosec: int
    display_image_url: str
    display_name: str
    is_blocked: bool
    last_successful_interation_utc_timestamp_nanosec: int
    wallet_id: str
    def __init__(self, display_name: _Optional[str] = ..., wallet_id: _Optional[str] = ..., display_image_url: _Optional[str] = ..., contact_added_utc_timestamp_nanosec: _Optional[int] = ..., last_successful_interation_utc_timestamp_nanosec: _Optional[int] = ..., is_blocked: bool = ...) -> None: ...

class ContactsListAndUserInfo(_message.Message):
    __slots__ = ["contact_list_generated_utc_timestamp_nanosec", "contacts", "user_info"]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_LIST_GENERATED_UTC_TIMESTAMP_NANOSEC_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    contact_list_generated_utc_timestamp_nanosec: int
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]
    user_info: Contact
    def __init__(self, user_info: _Optional[_Union[Contact, _Mapping]] = ..., contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]] = ..., contact_list_generated_utc_timestamp_nanosec: _Optional[int] = ...) -> None: ...

class StoredData(_message.Message):
    __slots__ = ["contacts_list_and_user_info"]
    CONTACTS_LIST_AND_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    contacts_list_and_user_info: ContactsListAndUserInfo
    def __init__(self, contacts_list_and_user_info: _Optional[_Union[ContactsListAndUserInfo, _Mapping]] = ...) -> None: ...
