"""
drop down:
----------
*a DD is set of options/collection of options.
*DD is classified into 2 types,
1.standard drop down
2.non-standard drop down

1.standard drop down:
---------------------
*a DD which is developed by select tag then it is called as standard drop down.
*it is classified into 2 types,
1.single select drop down(SSDD)
2.multi select drop down(MSDD)

1.single select drop down(SSDD)
*******************************
*we can select only one option
*we can't select multiple options
*we can't deselect the option

2.multi select drop down(MSDD)
*******************************
*we can select one option
*we can select multiple options
*we can deselect the option

how to automate standard drop down:
-----------------------------------
*to automate standard DD we use "select class", select class constructor will accept
drop down address as an argument.
*we need to import select class from below
    from selenium.webdriver.support.select import Select

class Select:
    def __init__(self, WebElement):
        ...

s = Select(WebElement)          #WebElement --> address of drop down    

*to select option there are 3 methods are present,
1.select_by_index(index_number)   #index number starts from 0
2.select_by_value("value attribute, value")
3.select_by_visible_text("text of an option")

*to de-select option there are 4 methods are present,
1.deselect_by_index(index_number)   #index number starts from 0
2.deselect_by_value("value attribute, value")
3.deselect_by_visible_text("text of an option")
4.deselect_all()

note: if we try to deselect for SSDD then it will throw "NotImplementedError"
"""
#sample html code
"""
<html>
          <body bgcolor="pink">
	Subject:<select id="s1">
		<option value="v1">MANUAL</option>
		<option value="v2">SQL</option>
		<option value="v3">PYTHON</option>
		<option value="v4">SELENIUM</option>
		<option value="v5">API</option>
	</select>
	Topic:<select id="s2" multiple>
		<option value="v11">SDLC</option>
		<option value="v22">QUERY</option>
		<option value="v33">PROGRAMS</option>
		<option value="v44">SCRIPTS</option>
		<option value="v55">DEFECT</option>
	</select>
          </body>
</html>
"""

from selenium.webdriver.support.select import Select

# ws to select option in SSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
ssdd = driver.find_element("id", "a1")
s = Select(ssdd)
s.select_by_index(2)
s.select_by_value("v4")
s.select_by_visible_text("Manual")
"""
# example on invalid index
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
ssdd = driver.find_element("id", "a1")
s = Select(ssdd)
s.select_by_index(22)
#NoSuchElementException
"""
# ws to select multiple option in MSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
msdd = driver.find_element("id", "a2")
s = Select(msdd)
s.select_by_index(2)
s.select_by_value("v11")
s.select_by_visible_text("Query")
"""
# ws to select multiple option and deselect in MSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
msdd = driver.find_element("id", "a2")
s = Select(msdd)
s.select_by_index(2)
s.select_by_value("v11")
s.select_by_visible_text("Query")
sleep(1)
s.deselect_by_index(1)
s.deselect_by_value("v11")
s.deselect_by_visible_text("Programs")
"""
# ws to select multiple option and deselect in MSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
msdd = driver.find_element("id", "a2")
s = Select(msdd)
s.select_by_index(2)
s.select_by_value("v11")
s.select_by_visible_text("Query")
sleep(1)
s.deselect_all()
"""
# example on deselect option in SSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
ssdd = driver.find_element("id", "a1")
s = Select(ssdd)
s.select_by_index(2)
sleep(1)
s.deselect_by_index(2)
#NotImplementedError: You may only deselect options of a multi-select
"""
##########################################################################################
# ws to select day,month and year option from facebook signup page
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Create new account']").click()
sleep(2)
day_dd = driver.find_element("id", "day")
s = Select(day_dd)
s.select_by_index(14)
month_dd = driver.find_element("name", "birthday_month")
s1 = Select(month_dd)
s1.select_by_value("7")
year_dd = driver.find_element("id", "year")
s2 = Select(year_dd)
s2.select_by_visible_text("1947")
"""
#####################################################################################
# select class methods
# --------------------

# is_multiple: it will return True if a DD is MSDD else it will return None.
# syntax: s.is_multiple

# ws to check subject and topic DD is MSDD or not
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
sub = driver.find_element("id", "a1")
s1 = Select(sub)
print(s1.is_multiple)               #None
top = driver.find_element("id", "a2")
s2 = Select(top)
print(s2.is_multiple)               #True
"""

# options: it will list of all options(webelement) address
# to get the correct o/p we should run for loop and .text property.
# it will work for both SSDD and MSDD
# syntax: s.options

# example on options property
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
sub = driver.find_element("id", "a1")
s = Select(sub)
options = s.options
print(options)
#[<selenium.webdriver.remote.webelement.WebElement (session="194c667d7e593da37ab56babb505a253", element="f.FED8ABDA51B7257828E1753EA128345E.d.1D22AC0A95D007AC1332A1EE2B169E33.e.4")>, <selenium.webdriver.remote.webelement.WebElement (session="194c667d7e593da37ab56babb505a253", element="f.FED8ABDA51B7257828E1753EA128345E.d.1D22AC0A95D007AC1332A1EE2B169E33.e.6")>, <selenium.webdriver.remote.webelement.WebElement (session="194c667d7e593da37ab56babb505a253", element="f.FED8ABDA51B7257828E1753EA128345E.d.1D22AC0A95D007AC1332A1EE2B169E33.e.8")>, <selenium.webdriver.remote.webelement.WebElement (session="194c667d7e593da37ab56babb505a253", element="f.FED8ABDA51B7257828E1753EA128345E.d.1D22AC0A95D007AC1332A1EE2B169E33.e.10")>, <selenium.webdriver.remote.webelement.WebElement (session="194c667d7e593da37ab56babb505a253", element="f.FED8ABDA51B7257828E1753EA128345E.d.1D22AC0A95D007AC1332A1EE2B169E33.e.12")>]
"""

# ws to print all the options present in subject DD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
sub = driver.find_element("id", "a1")
s = Select(sub)
ops = s.options     #ops = [webelement1, webelement2, webelement3, ..]
for i in ops:       #i=webelement1
    print(i.text)
# SQL
# Manual
# Selenium
# Python
# Api
"""

# all_selected_options: it will list of all selected options(webelement) address
# to get the correct o/p we should run for loop and .text property.
# it will work for both SSDD and MSDD, but prefer from MSDD.
# syntax: s.all_selected_options

# ws to print all selected options present in topic DD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
top = driver.find_element("id", "a2")
s = Select(top)
s.select_by_index(0)
s.select_by_index(2)
s.select_by_index(4)
ops = s.all_selected_options
for i in ops:
    print(i.text)
# Testcase
# Programs
# SDLC
"""
# ws to print all the amazon categories options
"""
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
dd = driver.find_element("id", "searchDropdownBox")
s = Select(dd)
ops = s.options
for i in ops:
    print(i.text)
# All Categories
# Alexa Skills
"""
# ws to print all months name from facebook
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Create new account']").click()
month_dd = driver.find_element("name", "birthday_month")
s1 = Select(month_dd)
all_opts = s1.options
for i in all_opts:
    print(i.text)
"""




