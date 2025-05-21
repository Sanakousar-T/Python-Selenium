
"""
verification property
"""
# title:
#   it will return the current title of a webpage.
#   syntax:
#       driver.title

from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to print title of myntra webpage

driver = Chrome(options=o)
driver.get("https://www.myntra.com/")
driver.maximize_window()
data = driver.title
print(data)
driver.close()
# Online Shopping for Women, Men, Kids Fashion & Lifestyle - Myntra

# -----------------------------------------------------------------------------
# current_url:
#   it will return current URL of a webpage.
#   syntax:
#       driver.current_url
# ws to print url of a webpage

driver = Chrome(options=o)
driver.get("https://www.myntra.com/")
driver.maximize_window()
data = driver.current_url
print(data)
driver.close()
# https://www.myntra.com/

# -----------------------------------------------------------------------------
# page_source:
#   it will return current webpage html source code
#   syntax:
#       driver.page_source

# ws to print current webpage source code

driver = Chrome(options=o)
driver.get("https://www.myntra.com/")
driver.maximize_window()
data = driver.page_source
print(data)
driver.close()
# <html> ... </html>
