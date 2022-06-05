import os
import time
import logging

from globals import ROOT_DIR
from datetime import datetime

logger = logging.getLogger(__name__)


class ConsolePrinter():
    pass


class LogfilePrinter():
    
    def __init__(self, log_dir):
        self.log_dir = log_dir
        self.log = None


    def create_directory(self, test_name):
        os.makedirs(ROOT_DIR + '/logs/' + test_name + '/' + str(get_time().replace(':', ';')))


    def open(self):

        os.mkdir(str(self.log_dir))
        self.log = open(str(self.log_dir), "w+")


    def print_log():
        pass




def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class Logger():
    
    def __init__(self):
        self.start_time = time.time()
        self.console_printer = ConsolePrinter()
        self.logfile_printer = LogfilePrinter()


LP = LogfilePrinter('xdd123')
LP.create_directory('test_login_valid_user')

