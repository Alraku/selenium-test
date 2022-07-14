from selenium import webdriver
from selenium.webdriver.edge.options import Options

from utils.logger import logger

options=Options()

driver = webdriver.Remote(
   command_executor='http://192.168.1.10:4444/wd/hub',options=options)

driver.get("https://github.com")
print(driver.title)
assert "GitHub" in driver.title
driver.quit()




