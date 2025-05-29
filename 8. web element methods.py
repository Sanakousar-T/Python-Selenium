"""
webelements:
************
*an element present in webpage is called as webelement.
*the return type of find_element() method is webelement.
syntax:
-------
    variable = driver.find_element()
       \\
      webelement
"""
# send_keys(): it is used to enter a data into any textfield.
#   syntax:
#       web_element.send_keys("data")

# click():  it is used to click any element.
#   syntax:
#       web_element.click()

# clear(): it is used to remove the data present in any text field.
#   syntax:
#       web_element.clear()

# ws to enter selenium, remove and enter python selenium in un text field
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
un = driver.find_element("name", "email")
un.send_keys("selenium")
sleep(2)
un.clear()
sleep(2)
un.send_keys("python selenium")
"""

# get_attribute(): it will return specified attribute value of an element.
#                  if specified attribute is not present, then it will return None.
#   syntax:
#       web_element.get_attribute("attribute_name")

# ws to print gmail link href value
"""
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
g = driver.find_element("xpath", "(//a)[22]")
data = g.get_attribute("href")
print(data)                     #https://www.google.com/preferences?hl=en-IN&fg=1
"""
# example on attribute not matches
"""
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
g = driver.find_element("xpath", "(//a)[22]")
data = g.get_attribute("value")
print(data)             #None
"""
#ws to print tool tip of english link in wikipedia
"""
driver = Chrome(options=o)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
eng = driver.find_element("xpath", "(//a[@href='//en.wikipedia.org/'])[1]")
data = eng.get_attribute("title")
print(data)             #English — Wikipedia — The Free Encyclopedia
"""
###############################################################################################
# location: it will return dictionary of x and y axis of specific element in webpage
#   syntax:
#       web_element.location

# size: it will return dictionary of height and width  of specific element in webpage
#   syntax:
#       web_element.size

# rect: it will return dictionary of height, width x and y axis of specific element in webpage
#   syntax:
#       web_element.rect

# ws to return height, width x and y axis
"""
driver = Chrome(options=o)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
eng = driver.find_element("xpath", "(//a[@href='//en.wikipedia.org/'])[1]")
data1 = eng.location
print(data1)            #{'x': 464, 'y': 137}
data2 = eng.size
print(data2)            #{'height': 46, 'width': 156}
data3 = eng.rect
print(data3)            #{'height': 46, 'width': 156, 'x': 463.90625, 'y': 137.25}
"""

################################################################################################

# tag_name: it will return tag name of specific element in webpage
#   syntax:
#       web_element.tag_name

# ws to print tag name of english link in wikipedia.com
"""
driver = Chrome(options=o)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
eng = driver.find_element("xpath", "(//a[@href='//en.wikipedia.org/'])[1]")
print(eng.tag_name)         #a
"""
###############################################################################################
# text: it will return text of specific element in webpage.
#   syntax:
#       web_element.text

# ws to print text of customer services in amazon
"""
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
eng = driver.find_element("xpath", "//a[@data-csa-c-content-id='nav_cs_help']")
print(eng.text)         #Customer Service
"""
# ws to print text of movie name in book my show
"""
driver = Chrome(options=o)
driver.get("https://in.bookmyshow.com/bengaluru/movies/chhaava/ET00408691")
driver.maximize_window()
eng = driver.find_element("xpath", "//h1[@class='sc-qswwm9-6 jevoyi']")
print(eng.text)         #Chhaava
"""
################################################################################################
# sample html code
"""
<html>
          <body bgcolor="pink">
	UN1:<input type="text" id="a1">
	UN2:<input type="text" id="a2" disabled><hr/>
	<input type="checkbox" id="c1">NewUser
	<input type="checkbox" id="c2" checked>OldUser<hr/>
	<a href="https://www.fb.com" id="l1">Facebook</a>
	<a href="https://www.google.com" id="l2">Google</a>
          </body>
</html>
"""
# is_enabled(): it is will return True if element is enabled else it will return False.
#   syntax: 
#       web_element.is_enabled()

# ws to verify textfield is enabled or not
"""
driver = Chrome(options=o)
driver.get("file:///D:\Qspider\Python selenium\github selenium\sample.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un2 = driver.find_element("id", "a2")
print(un1.is_enabled())     #True
print(un2.is_enabled())     #False
"""

# ws to verify signin and sendotp button is enabled or not
"""
driver = Chrome(options=o)
driver.get("https://www.dunzo.com/bangalore")
driver.maximize_window()
signin = driver.find_element("xpath", "//p[.='Sign in']")
print(signin.is_enabled())              #True
signin.click()
otp = driver.find_element("xpath", "//button[.='Send OTP']")
print(otp.is_enabled())                 #False
"""
#############################################################################################
# is_selected(): it will return True if checkbox/radio button is selected else it will return False
#   syntax:
#       web_element.is_selected()

# ws to verify checkbox is selected or not
"""
driver = Chrome(options=o)
driver.get("file:///D:\Qspider\Python selenium\github selenium\sample.html")
driver.maximize_window()
check1 = driver.find_element("id", "c1")
check2 = driver.find_element("id", "c2")
print(check1.is_selected())             #False
print(check2.is_selected())             #True
"""
# ws to verify a radio button is selected or not in passport seva
"""
driver = Chrome(options=o)
driver.get("https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request_locale=en")
driver.maximize_window()
radio1 = driver.find_element("id", "cpvLocation13")
radio2 = driver.find_element("id", "cpvLocationPO")
print(radio1.is_selected())             #False
print(radio2.is_selected())             #True
"""
#############################################################################################
# is_displayed(): it will return True is element is present in webpage else it will throw NoSuchElement exception.
#   syntax:
#       web_element.is_displayed()

# ws to verify link is present in webpage or not
"""
driver = Chrome(options=o)
driver.get("file:///D:\Qspider\Python selenium\github selenium\sample.html")
driver.maximize_window()
link1 = driver.find_element("id", "l1")
print(link1.is_displayed())             #True
link2 = driver.find_element("id", "l22")
print(link2.is_displayed())             #NoSuchElementException
"""