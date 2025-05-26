"""
assignment
----------
https://www.karnatakaone.gov.in/Info/Public/BangaloreOne
launch above application --> click on sign in link --> click on create an account link in sign in
--> enter all the details and click on register me
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.karnatakaone.gov.in/Info/Public/BangaloreOne")
driver.maximize_window()
driver.find_element("xpath","(//a[.='Sign In'])[2]").click()
driver.find_element("link text","Create an account").click()
driver.find_element("xpath", "//input[@name='PortalLoginName']").send_keys("sanakousar")
driver.find_element("name","Password").send_keys("sanakousar@123")
driver.find_element("id","ConfirmPassword").send_keys("sanakousar@123")
driver.find_element("id","FullName").send_keys("sanakousar T")
driver.find_element("name","EmailId").send_keys("sanakousar@gmail.com")
driver.find_element("xpath","//input[@name='MobileNumber']").send_keys("9867541232")
sleep(2)
#driver.find_element("xpath","//button[@class='btn']").click()
r = driver.find_element("xpath","//button[@class='btn']")
if r.is_enabled():
   r.click()
else:
    print("Register me button is not enable")
driver.close()
