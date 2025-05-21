# close():
#   it will close the current window/tab.
#   syntax:
#       driver.close()

# quit():
#   it will close complete browser.
#   syntax:
#       driver.quit()

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)


# example on close() method

driver = Chrome(options=o)
driver.get("https://www.instagram.com/")
sleep(1)
driver.close()

# example on quit() method
"""
driver = Chrome(options=o)
driver.get("https://www.instagram.com/")
sleep(1)
driver.quit()
"""