import unittest
from cyclotron.managers.files import FileManager
from cyclotron.managers import CriticalOperationException
from tempfile import mkdtemp,mktemp
from os.path import isfile, join


class FileManagerCase(unittest.TestCase):

    fm = None

    def init_fm(self):
        temp_file = mktemp()
        open(temp_file, 'w').close()

        self.fm = FileManager(temp_file)

    def test_init(self):
        with self.assertRaises(CriticalOperationException):
            FileManager('/unexistent_file')

        self.init_fm()

    def test_copy_into(self):

        self.init_fm()

        new_dir = mkdtemp()
        self.fm.copy_into(new_dir)

        self.assertTrue(isfile(self.fm.full_path))
        self.assertTrue(isfile(join(new_dir, self.fm.basename)))

    def test_move_into(self):

        self.init_fm()

        new_dir = mkdtemp()
        self.fm.move_into(new_dir)

        self.assertFalse(isfile(self.fm.full_path))
        self.assertTrue(isfile(join(new_dir, self.fm.basename)))

    def test_rename_to(self):
        self.init_fm()

        with self.assertRaises(CriticalOperationException):
            self.fm.rename_to(mktemp(prefix='another_dir/'))

        new_name = mktemp()
        self.fm.rename_to(new_name)
        self.assertTrue(isfile(join(self.fm.dirname, new_name)))


if __name__ == '__main__':
    unittest.main()
