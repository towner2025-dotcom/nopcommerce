import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.getcwd(), "configuration", "config.ini")
config.read(config_path)

class Read_Config:

    @staticmethod
    def get_admin_page_url():
        return config.get('admin Login info', 'admin_page_url')

    @staticmethod
    def get_user_name():
        return config.get('admin Login info', 'username')

    @staticmethod
    def get_user_password():
        return config.get('admin Login info', 'password12')

    @staticmethod
    def get_invalid_username():
        return config.get('admin Login info', 'invalid_username')
