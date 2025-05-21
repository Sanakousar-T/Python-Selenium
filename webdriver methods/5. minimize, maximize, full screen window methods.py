# maximize_window():
#   it is used to maximize the window.
#   syntax:
#       driver.maximize_window()

# minimize_window():
#   it is used to minimize the window.
#   syntax:
#       driver.minimize_window()

# fullscreen_window():
#   it is used to set a full-screen window.
#   syntax:
#       driver.fullscreen_window()

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to maximize, minimize and full screen the window.

driver = Chrome(options=o)
driver.get("https://www.instagram.com/")
sleep(1)
driver.maximize_window()
sleep(1)
driver.minimize_window()
sleep(1)
driver.maximize_window()
sleep(1)
driver.fullscreen_window()
sleep(1)
driver.close()
