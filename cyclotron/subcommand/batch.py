from cyclotron.managers import CriticalOperationException
from cyclotron.subcommand.manager_action import ManagerAction
from cyclotron.managers.batch import BatchManager
import logging

logger = logging.getLogger(__name__)

class BatchAction(ManagerAction):

    @staticmethod
    def add_subparser(subparsers):

        import_parser = subparsers.add_parser('jobimport', help='import job')
        import_parser.add_argument('jobname', help='associated jobname')
        import_parser.add_argument('--id', help='specific ID')
        import_parser.set_defaults(func=BatchAction.handle_import)

        init_parser = subparsers.add_parser('jobinit', help='job initialize')
        init_parser.add_argument('jobname', help='associated jobname')
        init_parser.set_defaults(func=BatchAction.handle_init)

    @staticmethod
    def handle_import(args):

        try:
            batch_manager = BatchManager(args.jobname)
            batch_manager.import_file(file_id=args.id)
        except CriticalOperationException as e:
            logger.error(e)

    @staticmethod
    def handle_init(args):

        try:
            batch_manager = BatchManager(args.jobname, create_dirs=True)
        except CriticalOperationException as e:
            logger.error(e)

