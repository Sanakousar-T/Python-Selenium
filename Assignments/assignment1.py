
"""
assignment:
-----------
launch --> https://demowebshop.tricentis.com/
click on register link --> enter all the details and click on register button
"""

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()

o.add_experimental_option("detach",True)

driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
sleep(2)
driver.find_element("class name","ico-register").click()
driver.find_element("id","gender-female").click()
driver.find_element("id","FirstName").send_keys("sanakousar")
driver.find_element("id","LastName").send_keys("T")
driver.find_element("id","Email").send_keys("sana@gmail.com")
driver.find_element("id","Password").send_keys("Sana@123")
driver.find_element("id","ConfirmPassword").send_keys("Sana@123")
sleep(4)
driver.find_element("id","register-button").click()
sleep(4)

driver.close()
