import common_utils
import skymel_chat_pb2
import logging
import os


class SkymelChatHelper(object):
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.stored_data = None

        self.__load_data()

    def get_contacts_list_and_user_info(self) -> skymel_chat_pb2.ContactsListAndUserInfo:
        return self.stored_data.contacts_list_and_user_info

    def add_contact(self, wallet_id: str, display_name="", display_image_url=""):
        contact = skymel_chat_pb2.Contact(display_name=display_name,
                                          wallet_id=wallet_id, display_image_url=display_image_url,
                                          contact_added_utc_timestamp_nanosec=common_utils.get_timestamp_now_ns())
        self.stored_data.contacts_list_and_user_info.append(contact)
        self.__save_data()

    def __load_data(self):
        with open(self.data_file_path, "rb") as infile:
            self.stored_data = skymel_chat_pb2.StoredData.FromString(infile.read())

    def __save_data(self):
        with open(self.data_file_path, "wb") as outfile:
            outfile.write(self.stored_data.SerializeToString())


class SkymelChatHelperSingleton(object):
    __instance = None

    def __init__(self):
        raise RuntimeError('Cannot instantiate directly.')

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            logging.info('Creating the SkymelChatHelper object')
            try:
                cls.__instance = SkymelChatHelper(
                    os.path.join(os.path.dirname(__file__), "data", "data.bin"))
            except Exception as e:
                logging.error(str(e))
            logging.info('Finished creating the SkymelChatHelper object')
        return cls.__instance


print(SkymelChatHelperSingleton.getInstance().get_contacts_list_and_user_info())
