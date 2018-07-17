import ConfigParser
import logging

DEFAULT = {
    'log_level': 'INFO',
}

logger = logging.getLogger('cyclotron')


class Configuration(object):

    def __init__(self):
        self.config = ConfigParser.ConfigParser(defaults=DEFAULT)
        self.config_file = self.config.read(self.get_locations())

        self.elastic_url = self.config.get('elastic', 'url')

        self.log_level = self.config.get('logger', 'log_level')

    def get_locations(self):
        return './cyclotron.conf', '/etc/cylotron.conf'

    def set_logger(self):
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

        output = logging.StreamHandler()
        output.setFormatter(formatter)
        output.setLevel(logging.DEBUG)

        logger.addHandler(output)
