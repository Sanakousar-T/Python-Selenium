# 3. class name

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.myntra.com/")
driver.maximize_window()
driver.find_element("class name", "desktop-searchBar").send_keys("shirts")
driver.find_element("class name", "myntraweb-sprite.desktop-iconSearch.sprites-search").click()
sleep(2)
driver.close()

"""
note: only if class name value consist of any space then replace space with dot(.)
"""