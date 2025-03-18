import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getBaseURL():
        url = config.get("common value", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common value", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common value", "password")
        return password

    @staticmethod
    def get_incorrectUsername():
        incorrectUsername = config.get("common value", "incorrectUsername")
        return incorrectUsername