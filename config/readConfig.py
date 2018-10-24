from configparser import ConfigParser

class ReadCofig:
    def __init__(self):
        self.config=ConfigParser()
        self.config.read('./config.ini')

    def get_server(self,name):
        print(self.config.sections())
        value=self.config.get("testServer",name)
        return value
    def get_dbServer(self,username):
        value=self.config.get("DB",username)
        return value
