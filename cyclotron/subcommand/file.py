from cyclotron.subcommand.manager_action import ManagerAction
from cyclotron.managers.file import FileManager
import logging

logger = logging.getLogger(__name__)


class FileAction(ManagerAction):

    @staticmethod
    def add_subparser(subparsers):

        copy_parser = subparsers.add_parser('filecopy', help='file copy')
        copy_parser.add_argument('source', help='filename to handle')
        copy_parser.add_argument('destination', help='arguments', nargs='+')
        copy_parser.set_defaults(func=FileAction.handle_copy)

        move_passer = subparsers.add_parser('filemove', help='file move')
        move_passer.add_argument('source', help='filename to handle')
        move_passer.add_argument('destination', help='arguments', nargs='+')
        move_passer.set_defaults(func=FileAction.handle_move)

        rename_parser = subparsers.add_parser('rename', help='file rename')
        rename_parser.add_argument('source', help='filename to handle')
        rename_parser.add_argument('destination', help='arguments', nargs='+')
        rename_parser.set_defaults(func=FileAction.handle_rename)

    @staticmethod
    def handle_copy(args):

        try:
            file_manager = FileManager(args.filename)
            file_manager.copy_into(args.arguments[0])
        except Exception as e:
            logger.error(e)

    @staticmethod
    def handle_move(args):

        try:
            file_manager = FileManager(args.filename)
            file_manager.move_into(args.arguments[0])
        except Exception as e:
            logger.error(e)

    @staticmethod
    def handle_rename(args):
        try:
            file_manager = FileManager(args.filename)
            file_manager.rename_to(args.arguments[0])
        except Exception as e:
            logger.error(e)
