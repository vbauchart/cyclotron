import ConfigParser
import logging

logger = logging.getLogger(__name__)


CONFIG_LOCATION=(
    './cyclotron.conf',
    '/etc/cylotron.conf',
)

CONFIG_ENTRIES={

}

class GlobalConfiguration(object):

    def __init__(self, override={}):
        self.override = override

        self.config = ConfigParser.ConfigParser()
        self.config_file = self.config.read(CONFIG_LOCATION)
        self.conf_hash = {}


    def get_conf(self):
        self.elastic_url = self.config.get('elastic', 'url')
        self.log_level = self.config.get('logger', 'log_level')

