"""
action chains class:
--------------------
*action chains class used for following uses,
1.mouse hover action
2.drag and drop 
3.double click
4.right click

*action chains class should import from below
    from selenium.webdriver.common.action_chains import ActionChains
    
class ActionChains:
    def __init__(self, driver):
        ...

a = ActionChains(driver)

note:any method of action chains class should be end with .perform() method
"""

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)


# 1.mouse hover action:
# ---------------------
# keeping a cursor on an element is called as mouse hover action
# syntax: a.move_to_element(web_element).perform()

from selenium.webdriver.common.action_chains import ActionChains

# ws to mouse hover on learn tab and click on degree programs
"""
driver = Chrome(options=o)
driver.get("https://www.foundit.in/")
driver.maximize_window()
learn = driver.find_element("link text", "Learn")
a = ActionChains(driver)
a.move_to_element(learn).perform()
driver.find_element("link text", "Degree Programs").click()
"""
# ws to mouse hover on new featured tab in nike.com
"""
driver = Chrome(options=o)
driver.get("https://www.nike.com/in/")
driver.maximize_window()
ele = driver.find_element("xpath", "//button[.='New & Featured']")
a = ActionChains(driver)
a.move_to_element(ele).perform()
"""

###############################################################################################


# 2.drag and drop:
# ----------------
# dragging an element from position and dropping to another position is called as
# drag and drop
# syntax:
#   a.drag_and_drop(src_webelement, dest_webelement)

# ws to drag and drop
"""
driver = Chrome(options=o)
driver.get("https://pschool.in/science-3-sc/drag-drop-organs")
driver.maximize_window()
src1 = driver.find_element("xpath", "//div[.='Brain']")
dest1 = driver.find_element("xpath", "(//div[@class='blank '])[1]")
a = ActionChains(driver)
a.drag_and_drop(src1, dest1).perform()
src2 = driver.find_element("xpath", "//div[.='Heart']")
dest2 = driver.find_element("xpath", "(//div[@class='blank '])[2]")
a.drag_and_drop(src2, dest2).perform()
"""

#############################################################################################

# 3.double click:
# ---------------
# when ever we want to double click on an element then we use below methods of action chains class.
# syntax:
#   a.double_click(web_element).perform()

# ws to double click in demo webapplication
"""
driver = Chrome(options=o)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
double = driver.find_element("xpath", "//button[.='Double-Click Me To See Alert']")
a = ActionChains(driver)
a.double_click(double).perform()
"""

###############################################################################################

# 4.right click:
# to right on an element in a webpage we use below method.
# syntax:
#   a.context_click(webelement).perform()

# ws to right click on study material in byjus

"""
driver = Chrome(options=o)
driver.get("https://byjus.com/")
driver.maximize_window()
study = driver.find_element("link text", "Study Materials")
a = ActionChains(driver)
a.context_click(study).perform()
"""
#############################################################################################
"""
# mouse scrolling action:
# ---------------------
# syntax: a.scroll_to_element(web_element).perform()

driver = Chrome(options=o)
driver.get("https://www.foundit.in/")
driver.maximize_window()
learn = driver.find_element("xpath", "//a[.='Toll No: +91 80 6985 7811']")
a = ActionChains(driver)
a.scroll_to_element(learn).perform()
learn.click()
"""