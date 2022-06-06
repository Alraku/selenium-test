import time

from enum import Enum
from utils.helpers import get_time
from utils.logprinters import LogfilePrinter, ConsolePrinter


class Logger():

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    
    def __init__(self, test_name):
        self.start_time = time.time()
        #TODO self.console_printer = ConsolePrinter()
        self.logfile_printer = LogfilePrinter(test_name)


    def setup_logger(self):
        self.logfile_printer.open()


    def print_log(self, message, level):
        #TODO self.console_printer.print_log(message, level, get_time())
        self.logfile_printer.print_log(message, level, get_time())


    def info(self, message):
        self.print_log(message, Level.INFO)


    def error(self, message):
        self.print_log(message, Level.ERROR)


    def passed(self, message):
        self.print_log(message, Level.PASSED)


    def failed(self, message):
        self.print_log(message, Level.FAILED)


    def warning(self, message):
        self.print_log(message, Level.WARNING)


if "logger" not in globals():
    logger = Logger('test_login_valid_user')
    logger.setup_logger()


class Level(str, Enum):
    
    STEP = "STEP"
    INFO = "INFO"
    ERROR = "ERROR"
    PASSED = "PASS"
    FAILED = "FAIL"
    WARNING = "WARNING"