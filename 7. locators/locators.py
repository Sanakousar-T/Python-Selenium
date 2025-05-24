'''
locators:
---------
* finding/inspecting/searching/locating the path of an element in a webpage is called
as locators.
* all locators are belongs to "By" clas

why locators?
-------------
* before performing any action(entering, clicking, selecting,..) in a webpage first we
need to find the path of an element in a webpage because selenium is not a human it
doesn't know the path of element in a webpage.

types of locators:
------------------
1.id            5.link text
2.name          6.partial link text
3.class name    7.css selector
4.tag name      8.xpath

*to find an element in a webpage there are 2 methods are present,

1.find_element()                2.find_elements()

find_element():
---------------
* it is used to find single element in a webpage.
* the return type of find_element() is web element.
* if locator value matches with multiple element then it will return 1st element address.
* if the locator value not matches with any element then it will return "NoSuchElementException".

syntax:
    driver.find_element("locator_name", "locator_value")

find_elements():
----------------
*it is used to find multiple elements in a webpage.
"""

'''