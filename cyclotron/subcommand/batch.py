from cyclotron.subcommand.manager_action import ManagerAction
from cyclotron.managers.batch import BatchManager
import logging

logger = logging.getLogger(__name__)


class BatchAction(ManagerAction):

    @staticmethod
    def add_subparser(subparsers):

        action_choice = (
            'import',
        )
        parser = subparsers.add_parser('batch', help='file management')
        parser.add_argument('action', help='job action', choices=action_choice)
        parser.add_argument('jobname', help='associated jobname')
        parser.add_argument('--id', help='specific ID')
        parser.set_defaults(func=BatchAction.handle_action)

    @staticmethod
    def handle_action(args):

        try:
            batch_manager = BatchManager(args.jobname)
            if args.action == 'import':
                batch_manager.import_file(file_id=args.id)
            else:
                raise Exception('%s is not a correct argument' % args.action)
        except Exception as e:
            logger.error(e)
