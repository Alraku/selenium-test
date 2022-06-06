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
        self.log_dir = ROOT_DIR + '/logs/' + test_name
        self.log = None


    def create_directory(self):
        date_dir = get_time().replace(':', '-')
        os.makedirs(self.log_dir + '/' + date_dir)


    def open(self):
        if not os.path.exists(self.log_dir):
            self.create_directory()
        self.log = open(self.log_dir + '/' + self.log_file_name, "w+")


    def print_log(self, message, level, time_stamp):
        text_line = f'{time_stamp} - {level} - {message}\n'
        self.log.write(text_line)


class Logger():

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    
    def __init__(self):
        self.start_time = time.time()
        #TODO self.console_printer = ConsolePrinter()
        self.logfile_printer = LogfilePrinter('test_add_advert_basic')


    def print_log(self, message, level):
        #TODO self.console_printer.print_log(message, level, get_time())
        self.logfile_printer.print_log(message, level, get_time())


    def setup_logger(self):
        self.logfile_printer.open()


if "logger" not in globals():
    logger = Logger()
    logger.setup_logger()


class Level(Enum):
    
    STEP = "STEP"
    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"
    WARNING = "WARNING"