import os
import time

from enum import Enum
from utils.globals import ROOT_DIR
from datetime import datetime


def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%d__%H:%M:%S")


class ConsolePrinter():
    pass


class LogfilePrinter():
    
    def __init__(self, test_name):
        self.log_file_name = 'LOG_TC#001.txt'
        date_dir = get_time().replace(':', '-')
        self.log_dir = os.path.join(ROOT_DIR, 'logs/', test_name, date_dir)
        self.log = None


    def create_directory(self):
        date_dir = get_time().replace(':', '-')
        os.makedirs(os.path.join(self.log_dir))


    def open(self):
        if not os.path.exists(self.log_dir):
            self.create_directory()
        self.log = open(os.path.join(self.log_dir, self.log_file_name), "w+")


    def print_log(self, message, level, time_stamp):
        text_line = f'{time_stamp} - {level} - {message}\n'
        self.log.write(text_line)


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


    def warning(self, message):
        self.print_log(message, Level.WARNING)


    def info(self, message):
        self.print_log(message, Level.INFO)


if "logger" not in globals():
    logger = Logger('test_login_valid_user')
    logger.setup_logger()


class Level(str, Enum):
    
    STEP = "STEP"
    INFO = "INFO"
    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"
    WARNING = "WARNING"