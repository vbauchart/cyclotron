from cyclotron.subcommand.manager_action import ManagerAction
from cyclotron.managers.file import FileManager
import logging

logger = logging.getLogger(__name__)


class FileAction(ManagerAction):

    @staticmethod
    def add_subparser(subparsers):

        action_choice = (
            'copy_into',
            'move_into',
            'rename_to',
        )
        parser = subparsers.add_parser('file', help='file management')
        parser.add_argument('action', help='what to do with the file', choices=action_choice)
        parser.add_argument('filename', help='filename to handle')
        parser.add_argument('arguments', help='arguments', nargs='+')
        parser.set_defaults(func=FileAction.handle_action)

    @staticmethod
    def handle_action(args):

        try:
            file_manager = FileManager(args.filename)
            if args.action == 'copy_into':
                file_manager.copy_into(args.arguments[0])
            elif args.action == 'move_into':
                file_manager.move_into(args.arguments[0])
            elif args.action == 'rename_to':
                file_manager.move_into(args.arguments[0])
            else:
                raise Exception('%s is not a correct argument' % args.action)
        except Exception as e:
            logger.error(e)
