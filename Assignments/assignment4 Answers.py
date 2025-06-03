"""

assignment questions:
==========================

https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request
ws to automate the complete register page
ws to print all passport office names in passport seva registration page

https://mybmtc.karnataka.gov.in/info-2/Pass+counters/en
ws to print all bus stations names

https://www.foundit.in/seeker/registration
ws to print all country code present in mobile number

"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.support.select import Select
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to automate the complete register page
"""
driver = Chrome(options=o)
driver.get("https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request")
driver.maximize_window()
podd = driver.find_element("id","dcdrLocation")
s = Select(podd)
s.select_by_visible_text("Bengaluru")
name = driver.find_element("id","givenName")
name.send_keys("sanakousar")
surname = driver.find_element("id","surname")
surname.send_keys("Tallihal")
dob = driver.find_element("name","dob")
dob.send_keys("21/08/1989")
email = driver.find_element("name","email")
email.send_keys("sana@gmail.com")
driver.find_element("xpath","//label[.='Yes']").click()
pwd = driver.find_element("name","pwd")
pwd.send_keys("sana@1234")
driver.find_element("name","confirmPwd").send_keys("sana@1234")
hintQues = driver.find_element("name","hintQues")
s = Select(hintQues)
s.select_by_index(1)
hintAns = driver.find_element("name","hintAns")
hintAns.send_keys("Hubli")
driver.find_element("id","frmSample_register").click()
driver.close()

"""


# ws to print all passport office names in passport seva registration page
"""
driver = Chrome(options=o)
driver.get("https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request")
driver.maximize_window()
driver.find_element("id","passOffice").click()
driver.find_element("xpath","//a[.='Passport Offices in India']").click()
po = driver.find_elements("xpath","(//tbody)[14]//a")
for i in po:
    print(i.text)
"""

# ws to print all bus stations names
"""
driver = Chrome(options=o)
driver.get("https://mybmtc.karnataka.gov.in/info-2/Pass+counters/en")
driver.maximize_window()
BS = driver.find_elements("xpath","//tbody//tr")
for i in BS:
    print(i.text)
    """

# ws to print all country code present in mobile number
"""
driver = Chrome(options=o)
driver.get("https://www.foundit.in/seeker/registration")
driver.maximize_window()
#there is no Dropdown
"""




