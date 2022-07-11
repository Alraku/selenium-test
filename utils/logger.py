import time

from enum import Enum
from utils.helpers import get_time
from utils.logprinters import LogfilePrinter, ConsolePrinter


class Logger():

    _instance = None
    start_time = None
    test_session_name = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    
    def __init__(self):
        self.start_time = time.time()
        self.test_session_name = get_time()
        self.console_printer = ConsolePrinter(f"test_session_{self.test_session_name}")
        self.logfile_printer = LogfilePrinter(f"test_session_{self.test_session_name}")
        self.logfile_printer.open()


    def __del__(self):
        del globals()['logger']


    def print_log(self, message, level, color = ''):
        time_stamp = get_time().replace('__', ' ')
        self.console_printer.print_log(message, level, time_stamp, color)
        self.logfile_printer.print_log(message, level, time_stamp)


    def info(self, message):
        self.print_log(message, Level.INFO)


    def step(self, message):
        self.print_log(message, Level.STEP, Color.BLUE)


    def error(self, message):
        self.print_log(message, Level.ERROR, Color.RED)


    def passed(self, message):
        self.print_log(message, Level.PASSED, Color.GREEN)


    def failed(self, message):
        self.print_log(message, Level.FAILED, Color.RED)


    def warning(self, message):
        self.print_log(message, Level.WARNING, Color.ORANGE)


if "logger" not in globals():
    logger = Logger()


class Level(str, Enum):
    
    STEP = "STEP"
    INFO = "INFO"
    ERROR = "ERROR"
    PASSED = "PASS"
    FAILED = "FAIL"
    WARNING = "WARNING"


class Color():

    GREEN = "\x1b[32;20m"
    RED = "\x1b[31;20m"
    BLUE = "\033[34m"
    ORANGE = '\033[33m'
    RESET = "\x1b[0m"