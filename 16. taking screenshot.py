"""
taking screenshot:
------------------
*while testing if TE find any defect then will take screenshot, because it is a proof
to show for developer we got defect.
*in selenium to take screenshot we have below method.
    driver.save_screenshot("filename.png")
*by default it will save in current location.
*if we want to save in particular location then need to specify the path.
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to save a screenshot(it will save in current location)
"""
driver = Chrome(options=o)
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.save_screenshot("defect1.png")
"""

# ws to save a screenshot and save in specified location
"""
driver = Chrome(options=o)
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.save_screenshot("../screenshots/defect1.png")
"""
"""
. --> current file
. --> navigating from current file to project level
/ --> forward navigation
"""
#######################################################################################

from datetime import datetime

# example on datetime module
"""
d = datetime.now()
print(d)            #2025-03-07 19:20:27.683570

d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
print(d)            #07-03-2025 19-22-13
"""
# ws to save screenshot and save file name with current date and time
"""
d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
driver = Chrome(options=o)
driver.get("https://www.karnatakaone.gov.in/")
driver.maximize_window()
driver.save_screenshot(f"../screenshot/{d}.png")
"""

# real time example1: on assert and take screenshot
"""
testcase:
--------
step1: open the browser and enter URL
step2: click on personal loan
step3: click on sign-in button
step4: click on investment and all investment
step5: close the browser
"""
"""
def verify_title(etitle):
    d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    assert driver.title==etitle, driver.save_screenshot(f"../screenshots/{d}.png")

driver = Chrome(options=o)
driver.get("https://www.bajajfinserv.in/")
driver.maximize_window()
driver.find_element("xpath", "//p[.='Personal Loan']").click()
verify_title("personal Loan - Apply for Instant Personal Loan Online Upto Rs. 55 lakh | Bajaj Finance")
driver.find_element("xpath", "//span[.='Sign In']").click()
verify_title("Login to Bajaj Finserv Customer Portal My Account")
driver.find_element("xpath", "//a[.='Investments']").click()
driver.find_element("link text", "All Investments").click()
verify_title("Start investing | Mutual funds | Fixed deposit")
"""
# real time example2: on assert and take screenshot
"""
testcase:
---------
step1: open the browser and enter URL
step2: click on tenders button
step3: click on recruitments
step4: click on recruitment regulation
step5: close the browser
"""

"""
from datetime import datetime

d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

driver = Chrome(options=o)
driver.get("https://www.esic.gov.in/")
driver.maximize_window()
driver.find_element("xpath", "//a[.=' Tenders']").click()
assert driver.title=="ESIC Tender | Employees' State Insurance Corporation", driver.save_screenshot(f"../screenshots/{d}.png")
driver.find_element("xpath", "//a[.=' Recruitments']").click()
assert driver.title=="ESIC Recruitments | Employees' State Insurance Corporation", driver.save_screenshot(f"../screenshots/{d}.png")
driver.find_element("link text", "Recruitment Regulations").click()
assert driver.title=="Recruitment Regulations | Employee's State Insurance Corporation, Ministry of Labour & Employment, Government of India", driver.save_screenshot(f"../screenshots/{d}.png")
driver.close()
"""