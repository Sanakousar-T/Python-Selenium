"""
assignment
=========
1)https://www.nseindia.com/
inspect stock price of NIFTY NEXT 50

2)https://www.accuweather.com/en/in/india-weather
inspect weather of Bengaluru

3)https://www.goodreturns.in/gold-rates/
inspect price of 22K gold

4)https://www.barcindia.co.in/data-insights
inspect TRP of Sun TV
(//td[contains(., 'Sun TV')]/..//td)[3]
"""

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

driver1 = Chrome(options=o)
driver1.get("https://www.nseindia.com/")
driver1.maximize_window()
print(driver1.find_element("xpath","(//h3[@class='value'])[15]").text)
driver1.close()

driver2 = Chrome(options=o)
driver2.get("https://www.accuweather.com/en/in/india-weather")
driver2.maximize_window()
print(driver2.find_element("xpath","(//span[@class='text title no-wrap'])[2]/..").text)
driver2.close()

driver3 = Chrome(options=o)
driver3.get("https://www.goodreturns.in/gold-rates/")
driver3.maximize_window()
print(driver3.find_element("xpath","(//p[@class='gold-common-head'])[4]").text)
driver3.close()

driver4 = Chrome(options=o)
driver4.get("https://www.barcindia.co.in/data-insights")
driver4.maximize_window()
print(driver4.find_element("xpath","(//td[contains(.,'Sun TV')]/..)//td[3]").text)
driver4.close()
