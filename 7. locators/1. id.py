# 1. id:
#----------------------------------

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

# possiablity1: locator value matches with single element
'''
driver = Chrome(options=o)
driver.get("file:///D:\Qspider\Python selenium\github selenium\locators\demo.html")
driver.maximize_window()
#way1: store the address in a variable(web element)
un = driver.find_element("id", "a1")
un.send_keys("selenium@gmail.com")
#           (or)
#way2: directly perform the action
driver.find_element("id", "a1").send_keys("selenium@gmail.com")
'''

# possiablity2: locator value matches with multiple elements then it will retun 1st
#               element address
"""
driver = Chrome(options=o)
driver.get("file:///D:\Qspider\Python selenium\github selenium\locators\demo.html")
driver.maximize_window()
pwd = driver.find_element("id", "a1")
pwd.send_keys("selenium@123")
"""

# possiablity3: locator value not matches with any element
"""
driver = Chrome(options=o)
driver.get("file:///D:\Qspider\Python selenium\github selenium\locators\demo.html")
driver.maximize_window()
pwd = driver.find_element("id", "a11")
pwd.send_keys("selenium@123")
#NoSuchElementException
"""

# ws to enter username,password and click on login button in facebook.com

driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
un = driver.find_element("id", "email")
un.send_keys("selenium@gmail.com")
pwd = driver.find_element("id", "pass")
pwd.send_keys("selenium@123")
sleep(2)
login = driver.find_element("name", "login")
login.click()
driver.close()