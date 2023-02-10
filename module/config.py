import configparser
import os
from argparse import ArgumentParser, Namespace
from distutils.util import strtobool
from pathlib import Path

from dotenv import load_dotenv

config = configparser.ConfigParser()
load_dotenv()

ROOT_FOLDER = Path(__file__).absolute().parent.parent
CONFIGS_FOLDER = Path(ROOT_FOLDER, 'scripts/configs/')
CONFIG_FILE = Path(ROOT_FOLDER, 'config.ini')
config.read_file(CONFIG_FILE.open())
URL = os.environ['URL']

if not CONFIGS_FOLDER.exists():
    os.mkdir(CONFIGS_FOLDER)


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('--target', type=str, default=config['general']['TEST_TARGET'])
    parser.add_argument('--folder', '-f', type=str, default=config['general']['DEFAULT_SCRIPTS_FOLDER'])
    parser.add_argument('--proxies', default=config['general']['DEFAULT_PROXIES'], type=str)
    parser.add_argument('--threads', '-t', type=str, default=config['general']['THREADS_LIMIT'])
    parser.add_argument('--start', '-s', default=config['general'].get('START'), type=str)
    args = parser.parse_args()
    return args


TARGETS_HOST = config['general']['TARGETS_HOST']
PROXIES_HOST = config['general']['PROXIES_HOST']
TEXTS_HOST = config['general']['TEXTS_HOST']
LINKS_HOST = config['general']['LINKS_HOST']
REFERRALS_HOST = config['general']['REFERRALS_HOST']
LOGGING_LEVEL = config['general'].getint('LOGGING_LEVEL')

CAPMONSTER_HOST = os.environ.get('CAPMONSTER_HOST')
ZENNO_KEY = os.environ['ZENNO_KEY']

ARGS = get_args()
TEST_TARGET = ARGS.target
THREADS_LIMIT = ARGS.threads
SCRIPTS_FOLDER = ARGS.folder
PROXIES = ARGS.proxies
START = bool(strtobool(ARGS.start))
