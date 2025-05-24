# 4. tag name

"""
        attribute name  attribute value
            //               //
<a         href="https://www.google.com"     id="a1"     class="c1">  Google <a/>
 \\                    \\                         \\           \\       \\
1.tag name        2.attribute1               attribute2   attribute3   3.text

there are 3 components of html code,
====================================
1.tag name: anything which begins with angular brackets are called tag name
2.attribute: anything LHS=RHS are called attribute
3.text: anything which begins before close tag are called text
"""

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to enter data in username

driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/e6batch.html")
driver.maximize_window()
driver.find_element("tag name", "input").send_keys("selenium")

"""
note: tag name is not a preferable locator for find_element() method, it is best for 
"""
    