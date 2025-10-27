"""
synchronization:
----------------
*the process if matching selenium speed with application speed is called as synchronization.
                    (or)
*the process of matching selenium and application wavelength is called as synchronization.

*we can synchronization in 4 ways,
1.sleep()
2.implicitly_wait()
3.WebdriverWait()
4.fluent wait()

1.sleep():
----------
*it is a method of time module.
*it is used to sleep/pause the execution.
*it will accept seconds as a time duration.
    from time import sleep
    sleep(seconds)

drawbacks:
----------
*to synchronize 'n' elements we should write 'n' times sleep() method, because of this
code length will get increase and there is no optimization
*if element is visible less than the specified time duration, but sleep method
will wait complete timeduration because of this execution will take more time.
"""
#########################################################################################
#ws to enter first name in demo webpage
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/loading.html")
driver.maximize_window()
driver.find_element("name", "fname").send_keys("selenium")
#ElementNotInteractableException
"""
#ws to enter first name in demo webpage
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/loading.html")
driver.maximize_window()
sleep(15)
driver.find_element("name", "fname").send_keys("selenium")
"""

"""
2.implicitly_wait():
--------------------
*it is a method to synchronize find_element() and find_elements() method.
*it will accept seconds as a time duration.
*if the element is visible less than the specified time duration the remaining time will
be ignored.
*for 'n' element 1 implicitly wait method is sufficient.
*if the element is not visible within the specified time duration then it will throw
"NoSuchElementException"
    syntax: driver.implicitly_wait(seconds)
"""
#ws to enter first name in demo webpage
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/loading.html")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element("name", "fname").send_keys("selenium")
"""
#example on specifying lesstime in implicitly_wait()
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/loading.html")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element("name", "fname").send_keys("selenium")
#ElementNotInteractableException
"""
#ws to loginin to instagram.com
"""
driver = Chrome(options=o)
driver.get("https://www.instagram.com/accounts/login/?hl=en")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("name","username").send_keys("9988776655")
driver.find_element("name","password").send_keys("selenium@123")
driver.find_element("xpath","//div[.='Log in']").click()
"""
#ws to click on create account in twitter page
"""
driver = Chrome(options=o)
driver.get("https://x.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath", "//span[.='Create account']").click()
"""
########################################################################################
"""
3.webdriverwait/explicitwait:
#----------------------------
*it is a class which is used to synchronize title, url, text including find_element()
and find_elements() method.
*we need to import the class from below statement
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
*webdriverwait class constructor will accept driver and time duration as an argument.
*if the specified condition is False then it will throw TimeOutException.
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#ws to verify the twitter page
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath","//a[.='Twitter']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
assert driver.title=="nopCommerce (@nopCommerce) / X"
print("verification")
#AssertionError

*according to above script we will get AssertionError, bcz selenium very fastly checking the title, but application takes time to 
load, bcz of this getting Error.
*to sync title, URL, etc we use explicitwait.
"""
#titl_is: compelte title matches
#ws to verify title of twitter webpage
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath","//a[.='Twitter']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
wait = WebDriverWait(driver, 10)
wait.until(EC.title_is("nopCommerce (@nopCommerce) / X"))
print("verification")
#verification
"""
#example on title not matches
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath","//a[.='Twitter']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
wait = WebDriverWait(driver, 10)
wait.until(EC.title_is("nopCommerce (@nopCommerce)"))
print("verification")
#TimeoutException: Message
"""
#ws to verify title of twitter webpage
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath","//a[.='Twitter']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("nopCommerce"))
print("verification")
#verification
"""
#ws to verify title of twitter webpage
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath","//a[.='Twitter']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
wait = WebDriverWait(driver, 10)
wait.until(EC.url_to_be("https://x.com/nopCommerce"))
print("verification")
#verification
"""
#ws to verify title of twitter webpage
#title_contains : wait until the title contains in the main title
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath","//a[.='Twitter']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains("https://x.com"))
print("verification")
#verification
"""
#visibility_of_element_located : it will wait until the element is visible in webpage
"""
driver = Chrome()
driver.get("https://www.walmart.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located(("xpath", "//button[.='Services']")))
print("Element is visible in webpage")
"""
#text_to_be_present_in_element : it will wait until the text in the element is present or not
"""
driver = Chrome()
driver.get("https://www.dmartindia.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element(("xpath", "(//span[@class='MuiButton-label'])[2]"), "CATEGORIES"))
print("Text in Element is present")
"""
#################################################################################################################
"""
4.fluent wait:
--------------
*when the polling frequency is customize then it is called as fluent wait.
*by default is 0.5 second.
"""
"""
driver = Chrome()
driver.get("https://www.walmart.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10, poll_frequency=1)
"""
"""
what is the difference b/w implicitly wait and webdriver/explicit wait:
***********************************************************************
implicitly wait:
----------------
*it will synchronize only for find_element() and find_elements().
*it will throw "NoSuchElement Exception" if element is not visible within time duration.
*it is a method of browser class / web driver(no importing stmt).
*we will pass 1 argument that is time duration in seconds.
*we can't specify any conditions.

webdriver/explicit wait:
--------------
*it will synchronize all methods including find_element() and find_elements().
*it will throw "TimeOut Exception" if element is not visible within time duration.
*it is a method of WebDriverWait class, and also we need to specify the "expected_conditions"
we need to import both.
*we will pass two argument that is "driver and time duration".
*we will specify the conditions.
"""