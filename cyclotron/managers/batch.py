import logging
import yaml
import os
from cyclotron.config import GlobalConfiguration

logger = logging.getLogger(__name__)


class BatchManager(object):

    def __init__(self, job_name):
        self.job_name = job_name

        self.global_config = GlobalConfiguration()
        self.job_config = ''

        config_root = self.global_config.get_entry('batch', 'config_root')

        with open(os.path.join(config_root, '%s.yaml' % self.job_name)) as job_conf:
            self.job_config = yaml.load(job_conf)

    def import_file(self, file_id=None):
        print(self.job_config)
