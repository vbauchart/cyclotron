import ConfigParser
import logging

logger = logging.getLogger(__name__)

CONFIG_LOCATION = (
    './conf/cyclotron.conf',
    '/etc/cylotron/cyclotron.conf',
)

DEFAULT = {
    'main': {
        'log_level': 'INFO',
    },
    'batch': {
        'config_root': './conf/jobs/',
        'elastic_url': 'localhost',
    },
}


class GlobalConfiguration(object):

    def __init__(self, override={}):
        self.override = override

        self.config = ConfigParser.ConfigParser()
        self.config_file = self.config.read(CONFIG_LOCATION)
        self.conf_hash = {}

    def get_conf(self):
        # self.elastic_url = self.config.get('elastic', 'url')
        # self.log_level = self.config.get('logger', 'log_level')

        return DEFAULT

    def get_entry(self, section, option):

        if section in DEFAULT and option in DEFAULT[section]:
            return DEFAULT[section][option]
        else:
            return self.config.get(section, option)
