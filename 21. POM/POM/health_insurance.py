
class HeathInsurance:
    def __init__(self,driver):
        self.driver = driver
    def select_all_checkbox(self):
        self.driver.find_element("xpath", "//label[.='Select All']").click()
    def apply_now(self):
        self.driver.find_element("xpath", "(//a[.='Apply Now'])[4]").click()
    def get_quote(self):
        self.driver.find_element("xpath", "(//a[.='Get Quote'])[13]").click()
    def mobile_number(self, data):
        self.driver.find_element("name", "mobileNo").send_keys(data)
    def get_otp(self):
        self.driver.find_element("xpath", "//button[.='Get OTP']").click()


