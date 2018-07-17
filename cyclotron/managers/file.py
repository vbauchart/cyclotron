from shutil import copy, move
from os.path import isdir, dirname, basename, join, abspath, isfile
from cyclotron.managers import CriticalOperationException
import logging

logger = logging.getLogger(__name__)


class XFile


class FileManager(object):
    full_path = None
    dirname = None
    basename = None

    def __init__(self, path):
        self.full_path = abspath(path)
        self.dirname = dirname(self.full_path)
        self.basename = basename(self.full_path)

        if not isfile(self.full_path):
            raise CriticalOperationException('%s is not a valid file' % self.full_path)

    def copy_into(self, destination):
        if not isdir(destination):
            raise CriticalOperationException('%s is not a valid directory' % destination)

        logger.info('copying %s into %s' % (self.full_path, destination))
        copy(self.full_path, destination)

        return FileManager(join(destination, self.basename))

    def move_into(self, destination):
        if not isdir(destination):
            raise IOError('%s is not a valid directory' % destination)

        logger.info('moving %s into %s' % (self.full_path, destination))
        move(self.full_path, destination)

        return FileManager(join(destination, self.basename))

    def rename_to(self, destination):

        destination_dir = dirname(abspath(destination))
        if destination_dir != self.dirname:
            raise CriticalOperationException('%s is not in the same directory as %s' % (destination, self.full_path))

        logger.info('rename %s to %s' % (self.full_path, destination))
        move(self.full_path, destination)
