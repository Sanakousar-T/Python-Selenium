
class WelcomePage:
    def __init__(self,driver):
        self.driver = driver
    def loans(self):
        self.driver.find_element("xpath", "//li[contains(., 'Loans')]").click()
    def gold_loan(self):
        self.driver.find_element("xpath", "//span[.='Gold Loan']").click()
    def apply_online(self):
        self.driver.find_element("xpath", "(//a[.='Apply Online'])[3]").click()
    def insurance(self):
        self.driver.find_element("xpath", "(//li[contains(., 'Insurance')])[6]").click()
    def health_insurance(self):
        self.driver.find_element("xpath", "//span[.='Health Insurance']").click()
    def explore_plans(self):
        self.driver.find_element("xpath", "//a[.='Explore Plans']").click()







