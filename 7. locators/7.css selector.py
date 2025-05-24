# 7.css selector

"""
*css stands for cascading style sheet
*css is used for decorating a webpage like font, size, color, image, animation, effects, etc..
*in automation we will css expression.

sample html code:
-----------------
<a   href="https://www.gmail.com"   id="a1"   name="n1"> Gmail </a>
              |                        |          |
          attribute1              attribute2   attribute3

syntax:
-------
        tag_name[attribute_name = 'attribute_value']
        
example:
--------
        a[href = 'https://www.gmail.com']
        a[id = 'a1']
        a[name = 'n1']
        
steps to verify the css expression:
***********************************
step1: right click and inspect
step2: press ctrl+f --> now find by string search field will appear
step3: write css expression and press enter

if expression is valid verify the below things:
-----------------------------------------------
*the count should display 1of1
*element should be highlight
*code should be highlight in yellow color 

drawbacks:
----------
*we can't use text in css expression
*if css expression matches with multiple element then we can't get particular element expression
"""

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)


# ws to book a cab in rapido

driver = Chrome(options=o)
driver.get("https://www.rapido.bike/Home")
driver.maximize_window()
driver.find_element("css selector", "input[aria-label='pickup']").send_keys("rajajinagar metro")
sleep(2)
driver.find_element("css selector", "span[class='jsx-2715316807 main-text']").click()
driver.find_element("css selector", "input[aria-label='drop']").send_keys("majestic")
sleep(2)
driver.find_element("css selector", "span[class='jsx-2715316807 main-text']").click()
driver.find_element("css selector", "button[aria-label='book-ride']").click()
driver.close()
