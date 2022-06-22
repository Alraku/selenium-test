import os

from utils.helpers import get_time
from utils.globals import ROOT_DIR


class ConsolePrinter():

    def __init__(self, test_name):
        self.test_name = test_name

    
    def print_log(self, message, level, time_stamp, color):
        text_line = f'{time_stamp} - {color}{level} - {message}\x1b[0m'
        print(text_line)


class LogfilePrinter():
    
    def __init__(self, test_name):
        self.log_file_name = 'LOG_TC#001.txt'
        date_dir = get_time().replace(':', '-')
        self.log_dir = os.path.join(ROOT_DIR, 'logs/', test_name, date_dir)
        self.log = None


    def open(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.log = open(os.path.join(self.log_dir, self.log_file_name), "w+")


    def print_log(self, message, level, time_stamp):
        text_line = f'{time_stamp} - {level} - {message}\n'
        self.log.write(text_line)