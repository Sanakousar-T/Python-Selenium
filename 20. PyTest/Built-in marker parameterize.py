"""
parameterize:
-------------
@pytest.mark.parametrize: The builtin pytest.mark.parametrize decorator enables parametrization
of arguments for a test function.
Here is a typical example of a test function that implements checking that a certain input leads to an
expected output
note:
-----
*in "parametrize" the number of names must be equal to the number of values.

syntax:-
========
@pytest.mark.parametrize("value1, value2", [[val1, val2], [val3, val4],....])
def func(value1, value2):
     . . .

note:
-----
*no. of variable should be equal to no. of values.
*no. of test function call equal to no. of inputs/values.
*when ever we are declaring multiple variables then multiple variables should be enclosed within
any brackets like tuple, list, set.
"""

"""
def add():
    a = 10
    b = 20
    print(a+b)
add()       #30
add()       #30
"""

"""
def add(a, b):
    print(a+b)
add(4, 8)       #12
add(7, 1)       #8
add(9, 2)       #11
"""
#according to above function add is a normal function, it will accept parameters when we call a function.
#but if it is test function we can't pass a argument bcz test function are not explicitly callable.
#for any test function/method if we pass any argument then it will consider as a fixture.

"""
def test_add(a, b):
    print(a+b)
test_add(2, 3)
"""
"""
>pytest -vs pytestconcept.py
collected 1 item

pytestconcept.py::test_add ERROR
fixture 'a' not found
"""
#to over come above drawback we use "parameterize" as builtin marker.
"""
@pytest.mark.parametrize("a", [10, 20, 30, 40])
def test_add(a):
    print(f"input is {a}")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::test_add[10] input is 10
PASSED
pytestconcept.py::test_add[20] input is 20
PASSED
pytestconcept.py::test_add[30] input is 30
PASSED
pytestconcept.py::test_add[40] input is 40
PASSED
"""
#function level
"""
@pytest.mark.parametrize("a, b", [[10, 20], [2, 8], [8, 4]])
def test_add(a, b):
    print(f"result is:{a+b}")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_add[10-20] result is:30
PASSED
pytestconcept.py::test_add[2-8] result is:10
PASSED
pytestconcept.py::test_add[8-4] result is:12
PASSED
"""

"""
@pytest.mark.parametrize("a, b", [[10, 20], [2, 8], [8, 4]])
def test_add(c, b):
    print(f"result is:{c+b}")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items / 1 error

======================================================== ERRORS =========================================================
___________________________________________ ERROR collecting pytestconcept.py ___________________________________________
In test_add: function uses no argument 'a'
"""

"""
@pytest.mark.parametrize("a, b, c", [[10, 20], [2, 8], [8, 4]])
def test_add(a, b, c):
    print(f"result is:{a+b+c}")
"""
"""
>pytest -vs pytestconcept.py
pytestconcept.py::test_add: in "parametrize" the number of names (3):
  ['a', 'b', 'c']
must be equal to the number of values (2):
  [10, 20]
"""
#method level
"""
class Test_Demo:
    @pytest.mark.parametrize(["a", "b"], [["hey", "bye"], ["class", "over"]])
    def test_tc1(self, a, b):
        print(a, b)
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::Test_Demo::test_tc1[hey-bye] hey bye
PASSED
pyconcept.py::Test_Demo::test_tc1[class-over] class over
PASSED
"""
##########################################################################################
"""
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)

#ws to login for instagram.com with multiple set of inputs
"""
"""
@pytest.mark.parametrize("un, pwd", [["lokesh", "lokesh@1234"],
                                     ["mahesh", "mahesh@12123"],
                                     ["kumar", "kumar@!2334"]])
def test_login(un, pwd):
    driver = Chrome(options=o)
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("name", "username").send_keys(un)
    driver.find_element("name", "password").send_keys(pwd)
    driver.find_element("xpath", "//div[.='Log in']").click()
    sleep(3)
    driver.close()
"""