from shutil import copy, move
from os.path import isdir, dirname, basename, join, abspath, isfile
from cyclotron.managers import CriticalOperationException
import logging
from glob import glob
import os

logger = logging.getLogger(__name__)


class FilePatternSet(object):

    def __init__(self, glob_pattern, pick_order='filename'):
        self.glob_pattern = glob_pattern
        self.pick_order = pick_order
        self.fileset = []

        for path in glob(self.glob_pattern):
            self.fileset.append(FileManager(path))

    def pick_file(self):

        if len(self.fileset) == 0:
            raise CriticalOperationException('%s : no matching file' % self.glob_pattern)
        elif len(self.fileset) == 1:
            return self.fileset[0]
        else:
            if self.pick_order == 'filename':
                self.fileset.sort(reverse=True)
            elif self.pick_order == 'mtime':
                self.fileset.sort(key=lambda x: x.full_path, reverse=True)
            else:
                raise Exception('%s is not a valid pick strategy' % self.pick_order)

            for filemanager in self.fileset:
                logger.debug('%s is a candidate for %s' % (filemanager.full_path, self.glob_pattern))

            found_file = self.fileset[0]
            logger.info('%s selected for pattern %s' % (found_file.full_path, self.glob_pattern))

            return found_file


class FileManager(object):
    full_path = None
    dirname = None
    basename = None

    def __init__(self, path):

        self.full_path = path
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
