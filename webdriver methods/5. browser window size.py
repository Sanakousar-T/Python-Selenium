# get_window_size():
#   it will return dictionary of height and width of a browser.
#   syntax:
#       driver.get_window_size()

# get_window_position():
#   it will return dictionary of x and y-axis of a browser.
#   syntax:
#       driver.get_window_position()

# get_window_rect():
#   it will return dictionary of height, width, x and y-axis of a browser.
#   syntax:
#       driver.get_window_rect()

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to print x, y, width, height a of browser

driver = Chrome(options=o)
driver.get("https://www.ajio.com")
driver.maximize_window()
data = driver.get_window_size()
print(data)     # {'width': 1382, 'height': 744}
data1 = driver.get_window_position()
print(data1)    # {'x': -8, 'y': -8}
data2 = driver.get_window_rect()
print(data2)    # {'height': 744, 'width': 1382, 'x': -8, 'y': -8}
driver.close()

# set_window_size():
#   it is used to set the window based on height and width.
#   syntax:
#       driver.set_window(width, height)

# set_window_position():
#   it is used to set the window based on x and y axis.
#   syntax:
#       driver.set_window(x, y)

# set_window_rect():
#   it is used to set the window base on x, y, height and width.
#   syntax:
#       driver.set_window(x, y, width, height)

# ws to set the window based on x, y, width, height a of browser

driver = Chrome(options=o)
driver.get("https://www.ajio.com")
driver.maximize_window()
sleep(2)
driver.set_window_size(789, 445)
sleep(2)
driver.set_window_position(18, -110)
sleep(2)
driver.set_window_rect(-9, 234, 789, 112)
