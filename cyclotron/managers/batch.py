import logging
import yaml
import os
from cyclotron.config import GlobalConfiguration, ConfigurationException
from cyclotron.events.dispatcher import EventDispatcher
from cyclotron.managers.file import DirectoryManager, FilePatternSet

logger = logging.getLogger(__name__)
events = EventDispatcher()

class BatchManager(object):

    def __init__(self, job_name, create_dirs=False):
        self.job_name = job_name

        self.global_config = GlobalConfiguration()
        self.job_config = {}
        self.input = None
        self.archive = None
        self.working = None
        self.reject = None

        self.import_files = []
        self.import_file = None

        config_root = self.global_config.get_entry('batch', 'config_root')

        with open(os.path.join(config_root, '%s.yaml' % self.job_name)) as job_conf:
            self.job_config = yaml.load(job_conf).get('cyclotron')

        self.set_directories(create_dirs)

    def set_directories(self, create=False):
        try:
            dir_config = self.job_config['directories']
            self.input = DirectoryManager(dir_config['input'], create)
            self.archive = DirectoryManager(dir_config['archive'], create)
            self.working = DirectoryManager(dir_config['working'], create)
            self.reject = DirectoryManager(dir_config['reject'], create)
        except KeyError as e:
            raise ConfigurationException('missing job entry "cyclotron.directories.%s"' % e.message)

    def prepare_file(self):
        self.import_files = FilePatternSet(self.job_config['jobs']['import']['file_pattern'])
        self.import_file = self.import_files.pick_file()

        self.import_file.mov
