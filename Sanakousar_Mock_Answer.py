"""
mock question:
----------------

step1: Launch https://www.apollopharmacy.in/ website
step2: verify are you in welcome page
step3: click on search medicine field
step4: verify are you in search medicine page
step5:search for dolo 650 tablet and click on add button
step6:click on cart icon
step7: click on qty drop-down and select 4 as option
step8: click on proceed button
step9: enter mobile number and click on next arrow
step10: close the browser
note: do assertion by title/url not matches then take screenshot


Mock Question Solution By Sanakousar:
------------------------------------

"""
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime

o = ChromeOptions()
o.add_experimental_option("detach", True)


# assertion by title/url not matches then take screenshot
def verify_title(etitle):
    d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    assert driver.title == etitle, driver.save_screenshot(f"../screenshots/{d}.png")


# step1: Launch https://www.apollopharmacy.in/ website
driver = Chrome(options=o)
driver.get("https://www.apollopharmacy.in/")
driver.maximize_window()
driver.implicitly_wait(10)

# step2: verify are you in welcome page
ids = driver.window_handles
# print(type(ids))
# print(len(ids))
driver.switch_to.window(ids[0])
# selenium very quickly checking the title, but application takes time to load so we use explicitwait.
wait = WebDriverWait(driver, 10)
wait.until(ec.title_is("Online Medical Store, Online Medicine Order, Fastest Delivery - Apollo Pharmacy"))
verify_title(driver.title)
print("verified, it is welcome page")
# print(driver.title)

# step3: click on search medicine field
driver.find_element("xpath", "//div[.=' Search Medicines']").click()

# this is to test assertion and SS
title = "Online Medical Store, Online Medicine Order, Fastest Delivery - Apollo Pharmacy"

# step4: verify are you in search medicine page
ids = driver.window_handles
# print(len(ids))
driver.switch_to.window(ids[0])
wait = WebDriverWait(driver, 10)
wait.until(ec.url_contains("search-medicines"))
# verify_title(title)  # uncomment this line and comment nextline to test the working of assertion and screenshot
verify_title(driver.title)
print("verified, it is search medicine page")

# step5:search for dolo 650 tablet and click on add button
search = driver.find_element("id", "searchProduct")
search.send_keys("dolo 650")
driver.find_element("xpath", "//span[.='Add']").click()

# step6:click on cart icon
cart = driver.find_element("xpath", "//a[@aria-label='Cart Icon']")
cart.click()

# step7: click on qty drop-down and select 4 as option
qty = driver.find_element("xpath", "//div[@class='MedicineProductCard_optionHead__zOvKm']")
qty.click()
driver.find_element("xpath", "//p[.=4]").click()

# step8: click on proceed button
proceed = driver.find_element("xpath", "//span[.='Proceed']")
proceed.click()

# step9: enter mobile number and click on next arrow
# hidden division popup handling
driver.find_element("name", "mobileNumber").send_keys("9902136786")
driver.find_element("xpath", "(//button[@aria-label='Button'])[22]").click()

# step10: close the browser
driver.close()