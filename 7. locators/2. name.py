# 2.name

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to serach for english in wikipedi

driver = Chrome(options=o)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.find_element("name", "search").send_keys("english")
driver.find_element("class name", "pure-button.pure-button-primary-progressive").click()
sleep(2)
driver.close()

# ws to search for python selenium in google.com

driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element("name", "q").send_keys("python selenium")
sleep(2)
driver.close()