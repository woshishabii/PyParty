import json
import base64


class BasicDataHandler(object):
    def __init__(self, data):
        self.data = json.loads(base64.b64decode(data).decode('utf-8'))
    
    def handle(self):
        pass

