from welcome_page import *
from glod_loan_page import *

def test_TC1(launch):
    driver = launch
    w = WelcomePage(driver)
    w.loans()
    w.gold_loan()
    w.apply_online()
    g = GoldLoanPage(driver)
    g.enter_amount("50000")
    g.apply_now()
    g.enter_mobile_number("9988776655")
    g.get_otp()













