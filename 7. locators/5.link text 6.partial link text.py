# 5.link text

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

#ws to click on google link in demo webpage

"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/e6batch.html")
driver.maximize_window()
driver.find_element("link text", "Google").click()
"""

#ws to click on electronics in flipkart.com

"""
driver = Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element("link text", "Electronics").click()
"""

# example on text other than <a> tag
"""
driver = Chrome(options=o)
driver.get("https://www.rapido.bike/Home")
driver.maximize_window()
driver.find_element("link text", "Book Ride").click()
#NoSuchElementException
"""

#---------------------------------------------------------------------

#6.partial link text

driver = Chrome(options=o)
driver.get("https://www.amazon.in/s?rh=n%3A1389401031%2Cp_123%3A46655&dc&qid=1746195468&rnid=91049095031&ref=sr_nr_p_123_1")
driver.maximize_window()
driver.find_element("partial link text", "Samsung Galaxy M05").click()

"""
note:
-----
*both link text and partial link text will work only a text present in "<a>" or "<span>" inside 
a "<a>" tag.
*both are case sensitive.
*when the link text is very lengthy then we go partial link text.
"""