import inspect
from utils.logger import logger


logger.warning('Test warning')


def test_basic_one():
    print(inspect.stack()[0][3])

test_basic_one()