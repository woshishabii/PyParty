import os
import configparser


class BasicConfig(object):
    def __init__(self, filename='config.ini'):
        self.filename = filename
        self.data = configparser.ConfigParser()
        self.save = self.initial_new_config
        if os.path.exists(self.filename):
            self.load_config()
        else:
            self.initial_new_config()
    
    def initial_new_config(self):
        with open(self.filename, 'w') as f:
            self.data.write(f)
    
    def load_config(self):
        self.data.read(self.filename)
    
    def custom_config_through_shell(self):
        pass
