from cyclotron.managers import CriticalOperationException
from cyclotron.subcommand.manager_action import ManagerAction
from cyclotron.managers.batch import BatchManager
import logging

logger = logging.getLogger(__name__)

class BatchAction(ManagerAction):

    @staticmethod
    def add_subparser(subparsers):

        import_parser = subparsers.add_parser('batchimport', help='import batch')
        import_parser.add_argument('confname', help='associated configuration')
        import_parser.set_defaults(func=BatchAction.handle_import)

        init_parser = subparsers.add_parser('batchinit', help='job configuration')
        init_parser.add_argument('confname', help='associated jobname')
        init_parser.set_defaults(func=BatchAction.handle_init)

    @staticmethod
    def handle_import(args):

        try:
            batch_manager = BatchManager(args.confname)
            batch_manager.prepare_file()
            batch_manager.run_import()
        except CriticalOperationException as e:
            logger.error(e)

    @staticmethod
    def handle_init(args):

        try:
            batch_manager = BatchManager(args.confname, create_dirs=True)
        except CriticalOperationException as e:
            logger.error(e)

