import argparse
from cyclotron.config import Configuration
from cyclotron.subcommand.file import FileAction


conf = Configuration()


parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")

subparsers = parser.add_subparsers(help='available commands')

FileAction.add_subparser(subparsers)

args = parser.parse_args()
args.func(args)
