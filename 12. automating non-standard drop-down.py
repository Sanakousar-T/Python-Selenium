"""
non-standard dropdown:
----------------------
*a DD which is developed other than "select" tag then it is called as non-standard DD
*will automate non-standard DD by find_elements() method.
"""
#ws to print auto suggestion of google
"""
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element("name", "q").send_keys("python selenium")
sleep(2)
ops = driver.find_elements("xpath", "//div[@class='lnnVSe']")
for i in ops[:10]:
    print(i.get_attribute("aria-label"))
"""
#ws to print auto suggestion in amazon
"""
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element("id", "twotabsearchtextbox").send_keys("shirts")
sleep(2)
ops = driver.find_elements("xpath","//div[contains(@class, 'ellipsis-direction')]")
for i in ops:
    print(i.get_attribute("aria-label"))
"""
#ws toprint travel info in bmrcl
"""
driver = Chrome(options=o)
driver.get("https://english.bmrc.co.in/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "//span[.='English']").click()
driver.find_element("xpath", "//a[.='TRAVEL INFO']").click()
ops = driver.find_elements("xpath", "(//li[@class='nav-item'])[11]//a")
for i in ops:
    print(i.text)
"""