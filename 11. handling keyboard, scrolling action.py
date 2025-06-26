"""
handling keyboard actions:
--------------------------
*to handle keyboard actions we use "Keys" module from below statement.
    from selenium.webdriver.common.keys import Keys
*we should use send_keys() method to perform keyboard action.
    syntax: web_element.send_keys(Keys.key_name)
"""

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

from selenium.webdriver.common.keys import Keys

#ws to click on backspace
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
un = driver.find_element("id", "email")
un.send_keys("selenium")
un.send_keys(Keys.BACK_SPACE)
"""
#ws to perform backspace for 3 times
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
un = driver.find_element("id", "email")
un.send_keys("selenium")
for i in range(3):
    un.send_keys(Keys.BACKSPACE)
"""
#ws to clear the data without using clear() method
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
un = driver.find_element("id", "email")
un.send_keys("selenium")
un.send_keys(Keys.CONTROL+"a")
un.send_keys(Keys.BACKSPACE)
"""
#ws to enter selenium in UN and copy pate in PWD text field
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
un = driver.find_element("id", "email")
pwd = driver.find_element("id", "pass")
un.send_keys("selenium")
un.send_keys(Keys.CONTROL+"a")
un.send_keys(Keys.CONTROL+"c")
pwd.send_keys(Keys.CONTROL+"v")
"""
#ws to click on forgotten password without using click() method
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
link = driver.find_element("xpath", "//a[.='Forgotten password?']")
link.send_keys(Keys.ENTER)
"""

"""
scrolling a webpage:
--------------------
*to scroll in a webpage we use below method,
    ->driver.execute_script("window.scrollBy(x, y)")
    the above method will perform scroll down action
    ->driver.execute_script("window.scrollTo(x, y)")
    the above method will perform scroll up action    
"""
#ws to scroll down 500pixel
"""
driver = Chrome(options=o)
driver.get("https://www.decathlon.in/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 500)")
"""
#ws to scroll down 3times
"""
driver = Chrome(options=o)
driver.get("https://www.decathlon.in/")
driver.maximize_window()
for i in range(3):
    driver.execute_script("window.scrollBy(0, 500)")
"""
#ws to scroll down to free online eye test in lenskart
"""
driver = Chrome(options=o)
driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(2)
ele = driver.find_element("xpath", "//h4[.='Free Online Eye Test']")
d = ele.location            #d={'x': 40, 'y': 2239}
driver.execute_script(f"window.scrollBy({d['x']}, {d['y']})")
"""
#ws to scroll down and scroll up
"""
driver = Chrome(options=o)
driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(2)
driver.execute_script(f"window.scrollBy(0, 1700)")
sleep(2)
driver.execute_script("window.scrollTo(500, 0)")
"""
#ws to scroll down to trending sunglasses and scroll up to free online eye test
"""
driver = Chrome(options=o)
driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(2)
ele = driver.find_element("xpath", "//h4[.='Trending Sunglasses']")
d = ele.location            #d={'x': 40, 'y': 2239}
driver.execute_script(f"window.scrollBy({d['x']}, {d['y']})")
sleep(2)
ele = driver.find_element("xpath", "//h4[.='Free Online Eye Test']")
d = ele.location            #d={'x': 40, 'y': 2239}
driver.execute_script(f"window.scrollTo({d['x']}, {d['y']})")
"""
