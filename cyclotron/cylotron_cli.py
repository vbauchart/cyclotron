import argparse
from cyclotron.config import GlobalConfiguration
from cyclotron.subcommand.file import FileAction
from cyclotron.subcommand.log import LoggerAction
from cyclotron.subcommand.batch import BatchAction
from sys import argv
import logging
import colorlog
import os

def init_logger(level):
    """init the logger

    Args:
        level (str): level of log (debug, info, warn, error)
    """

    if "color" in os.environ.get("TERM", ""):
        console_formatter = colorlog.ColoredFormatter('%(log_color)s%(asctime)s:%(levelname)s: %(message)s')
        console_handler = colorlog.StreamHandler()
    else:
        console_formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')
        console_handler = logging.StreamHandler()

    console_handler.setFormatter(console_formatter)

    logger = logging.getLogger("cyclotron")
    logger.addHandler(console_handler)
    logger.setLevel(getattr(logging, level.upper()))

parser = argparse.ArgumentParser()
parser.add_argument("--log", help="set output verbosity", default='INFO')
subparsers = parser.add_subparsers(help='available commands')

FileAction.add_subparser(subparsers)
LoggerAction.add_subparser(subparsers)
BatchAction.add_subparser(subparsers)

args = parser.parse_args()

init_logger(args.log)
logger = logging.getLogger(__name__)

conf = GlobalConfiguration()

logger.debug('Starting %s' % argv)

args.func(args)
