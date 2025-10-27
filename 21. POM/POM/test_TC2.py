from welcome_page import *
from health_insurance import *

def test_TC2(launch):
    driver = launch
    w = WelcomePage(driver)
    w.insurance()
    w.health_insurance()
    w.explore_plans()
    h = HeathInsurance(driver)
    h.select_all_checkbox()
    h.apply_now()
    h.get_quote()
    h.mobile_number("9988776655")
    h.get_otp()




