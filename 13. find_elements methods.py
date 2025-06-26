# find_elements():
# ----------------
"""
*it is used to find multiple elements.
*the return type of find_elements() is list of webelement.
*if the locator value not matches with any element then it will return empty list[].
*to get the correct o/p we should run for loop and .text property

syntax:
    var_name = driver.find_elements("locator_name", "locator_value")
"""

# ws to print all link text present in demo webpage
"""
driver = Chrome(options=o)
driver.get("file:///D:\Qspider\Python selenium\github selenium\sample.html")
driver.maximize_window()
ops = driver.find_elements("tag name", "a")    #ops = [webelement1, webelement2, ..]
for i in ops:
    print(i.text)
# Facebook
# Google
"""

# example on locator value not matches with any element
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
ops = driver.find_elements("tag name", "b")    #ops = [webelement1, webelement2, ..]
print(ops)
#[]
"""

# ws to print total no. of links present in amazon webpage
"""
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
ops = driver.find_elements("xpath", "//a")
print(len(ops))         #338
"""

"""
xpath to to count total no. of links
//a
xpath to to count total no. of images
//img
xpath to to count total no. of text fields
//input
xpath to to count total no. of drop down
//select
"""

"""
what is the difference b/w find_element() and find_elements()
=============================================================
            find_element                    find_elements
            ------------                    -------------
*it is used to find single element      *it is used to find multiple elements
*return type is webelement              *return type is list of webelements
*if the locator value matches with      *if the locator value matches with
multiple elements then it will return   multiple elements then it will return
1st element address                     all elements address
*if locator value not matches           *if locator value not matches then it 
then it will throw NoSuchElement        will return empty list []
exception
"""