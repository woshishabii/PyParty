import pymysql
import sys

sys.path.append('..')
import pp_config


class BasicConnector(object):
    def __init__(self, config: pp_config.BasicConfig):
        self.host = config.data.data['db']['host']
        self.port = int(config.data.data['db']['port'])
        self.conn = pymysql.connect(self.host, self.port)