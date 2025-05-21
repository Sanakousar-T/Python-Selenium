# get():
#       it is used to enter the URL
#       it will accept both secured(https) and non-secured(http) URL.
#       if we pass other than secured and non-secured URL then it will throw, InvalidArgumentException
#   syntax: driver.get("URL")

from selenium.webdriver import Chrome, ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)

# example on secured URL

driver = Chrome(options=o)
driver.get("https://www.fb.com")

# example on non-secured URL
"""
driver = Chrome(options=o)
driver.get("http://www.fb.com")
"""
# example on invalid URL
"""
driver = Chrome(options=o)
driver.get("www.fb.com")
#InvalidArgumentException
"""