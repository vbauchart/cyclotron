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
            'debug',
        )
        parser = subparsers.add_parser('log', help='log management')
        parser.add_argument('level', help='log level', choices=action_choice)
        parser.add_argument('messages', help='filename to handle', nargs='+')
        parser.set_defaults(func=LoggerAction.handle_action)

    @staticmethod
    def handle_action(args):

        try:
            if args.level == 'info':
                logger.info(' '.join(args.messages))
            elif args.level == 'error':
                logger.error(' '.join(args.messages))
            elif args.level == 'debug':
                logger.debug(' '.join(args.messages))
            else:
                raise Exception('%s is not a correct argument' % args.level)
        except CriticalOperationException as e:
            logger.error(e)
            logger.error('Exiting')
            exit(1)
