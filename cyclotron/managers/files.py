from shutil import copy, move
from os.path import isdir, dirname, basename, join, abspath, isfile
from argparse import ArgumentParser
from cyclotron.managers import CriticalOperationException


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

        copy(self.full_path, destination)

        return FileManager(join(destination, self.basename))

    def move_into(self, destination):
        if not isdir(destination):
            raise IOError('%s is not a valid directory' % destination)

        move(self.full_path, destination)

        return FileManager(join(destination, self.basename))

    def rename_to(self, destination):

        destination_dir = dirname(abspath(destination))
        if destination_dir != self.dirname:
            raise CriticalOperationException('%s is not in the same directory as %s' % (destination, self.full_path))

        move(self.full_path, destination)


