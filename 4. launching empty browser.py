"""
launching empty browser:
------------------------
*to launch an empty browser developer has written code inside a browser-specific class
constructor.
*constructor will execute when ever we create an object
*each browser-specific class should be imported from the below statement.
    from selenium.webdriver import BrowserClassName
"""

"""
class Chrome:
    def __init__(self):
        #code to launch empty
        chrome browser

c = Chrome()            #object creation
"""
# ws to launch empty chrome browser
#from selenium.webdriver import Chrome
#c = Chrome()

# ws to launch empty firefox browser
# from selenium.webdriver import Firefox
# f = Firefox()

# ws to launch empty edge  browser
# from selenium.webdriver import Edge
# e = Edge()
###########################################################################################3
# program to with stand a Chrome browser for long duration
"""
*as per the latest version of selenium chrome browser will close automatically, if we
want to with stand a browser for long duration then we should follow the below code.  
"""
'''
from selenium.webdriver import Chrome, ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)

'''
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
