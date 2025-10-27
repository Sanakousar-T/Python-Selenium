
class GoldLoanPage:
    def __init__(self,driver):
        self.driver = driver
    def enter_amount(self, data):
        ele = self.driver.find_element("xpath", "//input[@aria-label='loan-amount-input']")
        ele.clear()
        ele.send_keys(data)
    def apply_now(self):
        self.driver.find_element("xpath", "//span[.='Apply Now']").click()
    def enter_mobile_number(self, data):
        self.driver.find_element("xpath", "//input[@id='otp-send-modal-mobile-input']").send_keys(data)
    def get_otp(self):
        self.driver.find_element("xpath","//button[.='GET OTP']").click()



