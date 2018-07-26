import logging
from string import Template

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

        config_root = self.global_config.get_entry('batch', 'config_root')
        self.job_config = BatchConfig(config_root, job_name=self.job_name, create=create_dirs)

        self.import_files = []
        self.import_file = None

    def prepare_file(self):
        self.import_files = FilePatternSet(self.job_config['jobs']['import']['file_pattern'])
        self.import_file = self.import_files.pick_file()

        #self.import_file.move_into(self.directories.get())


class BatchConfig(object):
    def __init__(self, config_root, job_name, create):
        self.directories = {}
        self.input_files = None
        self.command = None

        with open(os.path.join(config_root, '%s.yaml' % job_name)) as job_conf:
            job_config = yaml.load(job_conf).get('cyclotron')

        print(job_config['directories'])
        for name, fullpath in job_config['directories'].iteritems():
            try:
                self.directories[name] = self.resolve_variables(DirectoryManager(fullpath, create))
            except KeyError as e:
                raise ConfigurationException('missing job entry "cyclotron.directories.%s"' % e.message)

        self.input_files = self.resolve_variables(job_config['input_files'])
        self.command = self.resolve_variables(job_config['command'])

    def get_dir(self, name):
        return self.directories[name]

    def resolve_variables(self, value):
        s = Template(value).safe_substitute(self.directories)
        return s
