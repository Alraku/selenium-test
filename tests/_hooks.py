import os
import pytest
from datetime import datetime

start_time = datetime.strftime(datetime.now(), '%Y-%m-%d__%H-%M-%S')


@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    logging_plugin.set_log_path(
        os.path.join('logs', f'test_session_{start_time}', f'{item.name}.log'))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
