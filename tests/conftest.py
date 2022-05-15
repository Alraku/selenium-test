#coding: utf-8
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager


base_url = 'http://www.kurs-selenium.pl/demo'
mail_url = 'https://10minutemail.com'


@pytest.fixture(params=["edge", "safari"], scope='class')
#def setup(request, browser, url):
def setup(request):
    if request.param == "edge":
        driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()))
    elif request.param == "chrome":
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    elif request.param == "safari":
        driver = webdriver.Safari(service = Service(executable_path='/usr/bin/safaridriver'))

    #driver.get(url)
    driver.get('http://www.kurs-selenium.pl/demo/login')
    driver.maximize_window()
    request.cls.driver = driver
    
    yield driver
    driver.quit()


#this will get the value of CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


#This will return the browser value to setup method
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


#This will return the url value to setup method
@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")