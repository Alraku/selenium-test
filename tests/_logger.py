import pytest
import logging


@pytest.fixture(scope='session', autouse=True)
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    return logger


@pytest.fixture(autouse=True)
def logger_result(request, logger):
    test_case_name = request.node.name.upper()
    logger.info(f"Execution of Test Case: {test_case_name} has started.")

    def fin():
        logger.info(f"Execution of Test Case: {test_case_name} has ended.")
        logger.info(f"DURATION: {round(request.node.rep_call.duration, 2)} sec.")
        if request.node.rep_call.passed:
            logger.info("RESULT: PASSED")
        else:
            logger.info("RESULT: FAILED")

    request.addfinalizer(fin)
