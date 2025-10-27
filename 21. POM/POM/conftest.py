import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def launch():
    driver = Chrome()
    driver.get("https://www.bajajfinserv.in/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()






