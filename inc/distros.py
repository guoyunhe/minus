'''
Detect distribution name, version, etc.
Author: Guo Yunhe <i@guoyunhe.me>
'''

from configparser import ConfigParser

OS_RELEASE_PATH = '/etc/os-release'


class Distro:
    '''GNU/Linux Distribution Information'''

    def __init__(self):
        self._name = ''
        self._version = ''
        self._id = ''
        self._version_id = ''

    def read_os_release(self):
        '''Read & parse /etc/os-release'''
        with open(OS_RELEASE_PATH, 'r') as config_file:
            config_string = '[DEFAULT]\n' + config_file.read().replace('"', '')
        config = ConfigParser()
        config.read_string(config_string)
        default = config['DEFAULT']
        self._name = default.get('name')
        self._version = default.get('version')
        self._id = default.get('id')
        self._version_id = default.get('version_id')
        print(self._version_id)
