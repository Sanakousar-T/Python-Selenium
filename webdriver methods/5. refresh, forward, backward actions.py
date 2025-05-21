# back():
#   it used to click on backward arrow in the browser.
#   syntax:
#       driver.back()

# forward():
#   it used to click on forward arrow in the browser.
#   syntax:
#       driver.forward()

# refresh():
#   it used to click on refresh icon in the browser.
#   syntax:
#       driver.refresh()

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to perform backward, forward, refresh action in the browser.

driver = Chrome(options=o)
driver.get("https://www.flipkart.com")
driver.maximize_window()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
driver.close()
