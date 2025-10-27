"""
data-driven testing:
--------------------
"""
"""
from selenium.webdriver.support.select import Select
"""
"""
*testing an application with different set of input, reading data from excel is as
data driven testing.
*will store multiple set of inputs inside a excel file.
*since excel is a standalone application selenium will not support, so we use xlrd
as a 3rd plugin/application.

steps to install xlrd:
----------------------
click on left corner 4lines --> click on settings --> click on project --> click on python interpreter
click on + icon --> search for xlrd --> click on specify version checkbox --> select1.2.0 version
-->click on install package

steps to create a excel file in pycharm:
----------------------------------------
*create a directory in pycharm named as excel_file
*go to pycharm project location(right click on project-->click on open in --> click on explorer)
*click on excel_file folder
*create a new excel file(right click --> click on new --> click on microsoft excel)

steps to read data from excel file:
-----------------------------------
step1: open excel file
step2: specify the sheet name
step3: specify the row, colum number(both row and column index starts from 0)

method of extracting row and colum values
-----------------------------------------
row_values(row_num) : it will return list of the specified row all columns values
row_values(row_num, start_col): it will return list of specified row, from specified column
                            to till last column values
row_values(row_num, start_col, end_col): it will return list of specified row, from specified
start colum to specified end colum values
"""
"""
from xlrd import *
"""
#wp to print 4th row all columns
"""
#step1
wb = open_workbook("../excel_files/demo.xlsx")
#step2
sh = wb.sheet_by_name("Sheet1")
#step3
data = sh.row_values(3)
print(data)
#['simpledimple', 'simdim@12221']
"""
#wp to print 2nd row all columns
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
data = sh.row_values(2)
print(data)
#['test', 'test@12345', 'pass', 'fail']
"""
#wp to print 3rd row from 1st to last column
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
data = sh.row_values(2, 1)
print(data)
#['test@12345', 'pass', 'fail']
"""
#ws to print 3rd row 1st and 2nd column
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
data = sh.row_values(2, 0, 2)
print(data)
#['test', 'test@12345']
"""
#wp to print total number of rows and column
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows
print(row_count)            #6
col_count = sh.ncols
print(col_count)            #4
"""
#wp to print all username and password present in excel file
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows        #6
for i in range(row_count):  #[0, 1, .. 5]
    data = sh.row_values(i, 0, 2)
    print(data)
# ['username', 'password']
# ['demo', 'demo@123']
"""
#create a dictionary of username and password pair
"""
d = {}
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows                        #6
for i in range(row_count):                  #[0, 1, .. 5]
    data = sh.row_values(i, 0, 2)           #['username', 'password']
    d[data[0]] = data[1]
print(d)        #{'username': 'password', 'demo': 'demo@123', 'test': 'test@12345', 'simpledimple': 'simdim@12221', 'admin': 'manager', 'a1b2': '1a2b'}
"""
###############################################################################################
"""
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
"""
#ws to automate the facebook login page with different set of inputs
"""
d = {}    #{'demo': 'demo@123', 'test': 'test@12345', 'simpledimple': 'simdim@12221', 'admin': 'manager', 'a1b2': '1a2b'}
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows
for i in range(1, row_count):              #i=1
    data = sh.row_values(i)             #data=['demo', 'demo@123']
    d[data[0]] = data[1]

for un,pwd in d.items():                #[('demo','demo@123'), ('test','test@123')]
    driver = Chrome(options=o)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.find_element("id","email").send_keys(un)
    driver.find_element("id", "pass").send_keys(pwd)
    driver.find_element("name", "login").click()
    driver.close()
"""