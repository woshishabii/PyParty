import unittest
import sys
import os

# 初始化包环境
sys.path.append('..')
import server.pp_config


class TestConfigInitialLoad(unittest.TestCase):

    def test_create(self):
        self.config1 = server.pp_config.BasicConfig(filename='config1.ini')
        self.assertTrue(os.path.exists('config1.ini'))

    def test_load(self):
        self.config2 = server.pp_config.BasicConfig(filename='config2.ini')
        self.assertEqual(self.config2.data['DEFAULT'], {'password': '123456', 'a': '1', 'b': '2'})

if __name__ == '__main__':
    unittest.main()