# 8.xpath
"""
*path of an element in html tree structure is called as xpath.
*xpath is classified into 2 types

1.absolute xpath:
-----------------
*it indicates by single forward slash(/)
* (/) --> traverse from parent to its own child element.

2.relative xpath 
----------------
*it indicates by double forward slash(//)
* (//) --> traverse from parent to any child element.
"""
"""
sample html code:
-----------------
<html>
          <body bgcolor="pink">
	<div>
  	        UN1:<input type="text">
  	        UN2:<input type="text">
	</div>
	<div>
  	        UN3:<input type="text">
  	        UN4:<input type="text">
	</div>
          </body>
</html>
"""
#html tree
"""
html
  |
  |___body
        |
        |___div -->1
        |   |
        |   |__input -->1 (UN1) 
        |   |
        |   |__input -->2 (UN2)
        |
        |___div -->2
            |
            |__input -->1 (UN3)
            |
            |__input -->2 (UN4)
        
element name            absolute xpath                  relative xpath
===========             ==============                  ==============
UN1                     html/body/div[1]/input[1]       //div[1]//input[1]
UN2                     html/body/div[1]/input[2]       //div[1]//input[2]    
UN3                     html/body/div[2]/input[1]       //div[2]//input[1]
UN4                     html/body/div[2]/input[2]       //div[2]//input[2]
UN1, UN2                html/body/div[1]/input          //div[1]//input
UN3, UN4                html/body/div[2]/input          //div[2]//input
UN1, UN3                html/body/div/input[1]          //div//input[1] (or) //input[1]
UN2, UN4                html/body/div/input[2]          //div//input[2] (or) //input[2]
UN1, UN2, UN3, UN4      html/body/div/input             //div//input    (or) //input      
UN1, UN4                html/body/div[1]/input[1] |     //div[1]//input[1] | 
                        html/body/div[2]/input[2]       //div[2]//input[2]
UN2, UN3                html/body/div[1]/input[2] |     //div[1]//input[2]  |
                        html/body/div[2]/input[1]       //div[2]//input[1]
drawbacks of absolute xpath:
----------------------------
 * it will always traverse from parent to its own child.
 * xpath is very lengthy.
"""
"""
what is the difference b/w absolute xpath and relative xpath
************************************************************
    absolute xpath                      relative xpath
    ==============                      ===============
*indicated by single forward slash(/)   *indicated by double forward slash(//)
*/ -> it will traverse from parent to   *// -> it will traverse from parent to 
its own child                             any child
*xpath is very lengthy                  *xpath is short 
"""
# ---------------------------------------------------------------------------------------

"""
xpath by attribute:
===================
*inspecting an element by specifying attribute in xpath is called as xpath by attribute.

sample html code:
-----------------
<a   href="https://www.gmail.com"   id="a1"   name="n1"> Gmail </a>
              |                        |          |
          attribute1              attribute2   attribute3

syntax:
-------
//tagname[@attribute_name = 'attribute_value']

example:
--------
//a[@href='https://www.gmail.com']
//a[@id='a1']
//a[@name='n1']

xpath to inspect search field in lenskart
//input[@data-cy='searchInputField']

xpath to inspect signin button in swiggy
//a[@class='_5-C04']

xpath to inspect search field in olx.com
//input[@type='text']

xpath by multiple attributes
============================
*specifying multiple attributes in xpath is called as xpath by multiple attributes

syntax:
-------
//tagname[@attribute1='attribute_value1' and @attribute2='attribute_value2'...]

xpath to inspect mobiles in amazon.com
//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_mobiles']

xpath by group by index:
========================
*if xpath is matches with multiple elements to get the particular element then we go
xpath by group by index.
*index will starts from 1.
*write complete xpath in round brackets() and write index in square brackets[]

syntax:
-------
(xpath)[index]

xpath to inspect track order in lenskart
(//div[@class='ActionLink--pfnxg2 hlQiyT'])[1]

xpath to inspect mobile phones in olx.com
(//span[@data-aut-id='header_link'])[3]

xpath to inspect select location in bigbasket.com
(//button[@type='button'])[3]

xpath by text() function:
=========================
*inspecting and element by specifying text in xpath is called as xpath by text

sample html code:
-----------------
<a   href="https://www.gmail.com"   id="a1"   name="n1"> Gmail </a>
                                                            \\
                                                            text
syntax:
-------
//tagname[text() = 'text_value']
            (or)
//tagname[. = 'text_value']

example:
--------
//a[text() = 'Gmail']
        (or)
//a[.='Gmail']

xpath to inspect english link in wikipedia
//strong[text() = 'English']
        (or)
//strong[. = 'English']

xpath to inspect login button in zepto
//span[.='login']

xpath to inspect cafe in zepto
//span[.='Cafe']
"""
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)

# ws to login into irctc

driver = Chrome(options=o)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.find_element("xpath", "//a[.=' LOGIN ']").click()
driver.find_element("xpath", "//input[@placeholder='User Name']").send_keys("selenium")
driver.find_element("xpath", "//input[@placeholder='Password']").send_keys("selenium@123")
driver.find_element("xpath", "//input[@id='captcha']").send_keys("abcd123")
driver.find_element("xpath", "//label[.='Login & Booking With OTP']").click()
driver.find_element("xpath", "//button[.='Proceed']").click()
driver.find_element("xpath", "//button[.='SIGN IN']").click()
driver.close()