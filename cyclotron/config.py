import ConfigParser


class Configuration(object):

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config_file = self.config.read(self.get_locations())

        self.elastic_url = self.config.get('elastic', 'url')

    def get_locations(self):
        return ('./cyclotron.conf','/etc/cylotron.conf')