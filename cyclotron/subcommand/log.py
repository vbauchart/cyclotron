from cyclotron.subcommand.manager_action import ManagerAction
from cyclotron.managers import CriticalOperationException
import logging

logger = logging.getLogger(__name__)


class LoggerAction(ManagerAction):

    @staticmethod
    def add_subparser(subparsers):

        action_choice = (
            'info',
            'error',
        )
        parser = subparsers.add_parser('log', help='log management')
        parser.add_argument('level', help='log level', choices=action_choice)
        parser.add_argument('messages', help='filename to handle', nargs='+')
        parser.set_defaults(func=LoggerAction.handle_action)

    @staticmethod
    def handle_action(args):

        try:
            # logger_manager = LoggerManager()
            if args.level == 'info':
                logger.info(' '.join(args.messages))
            if args.level == 'error':
                logger.error(' '.join(args.messages))
            else:
                raise Exception('%s is not a correct argument' % args.action)
        except CriticalOperationException as e:
            logger.error(e)
            logger.error('Exiting')
            exit(1)
