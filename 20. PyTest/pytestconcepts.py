"""
pytest
"""
from time import sleep

import pytest
from selenium.webdriver.support.select import Select

"""
pytest:
*******
*pytest is a unit-testing framework basically developer will be used.
*pytest will be used by QA for following reason,
    *to run test function/method automatically.
    *to run multiple testcase at oneshot.
    *to generate reports.
    *to achieve parallel execution(compatibility).

steps to install pytest:
************************
click on file-->click on settings-->click on project-->click python interpreter-->click on plus icon
-->search for pytest-->click on specify version(latest version)-->click on install package.

naming convention for pytest:
*****************************
*function/method name should be starts with test keyword(test_*).
*class name should starts with Test keyword and 1st letter should be capital(Test_*) and pytest class should
not consist of constructor(__init__).
*module name can starts with test (or) end with test keyword(test_* (or) *_test).

how to run pytest function/class:
*********************************
*copy the path where pytest function/file is present(right click on folder-->click on copy path-->click on absolute path)
*open cmd --> change directory by below command
    >>cd path_of_pytest_file
    >>pytest -vs pytest_filename.py

v->verbosity
s->scripting    
*vs is used to get the output/message in detailed format.

right click on file --> click on open in -->click on terminal-->type the command

note:
-----
*a function which starts with test keyword is called as test function/method
*a class which starts with test keyword is called as test class.
*a module start/end with test keyword is called as test module.
"""

#calling a function
"""
def sample():
    print("sample testcase")

sample()
#sample testcase
"""

#calling a method
"""
class Demo:
    def simple(self):
        print("simple testcase")

d = Demo()
d.simple()
#simple testcase
""""""
*according to above example function and method will bet execute when ever we are calling explicitly.
*if we want to execute a function/method without calling explicitly then we need go for "pytest" concept.
"""
#####################################################################################################
#function level
#test function
"""
def test_TC1():
    print("testcase1 function")
def test_TC2():
    print("testcase2 function")
"""
"""
>pytest -vs pytestconcept.py
collected 2 items

pytestconcept.py::test_TC1 testcase1 function
PASSED
pytestconcept.py::test_TC2 testcase2 function
PASSED
"""
#non-test function
"""
def TC1_test():
    print("testcase1 function")
def test_TC2():
    print("testcase2 function")
"""
"""
>pytest -vs pytestconcept.py
collected 1 item

pytestconcept.py::test_TC2 testcase2 function
PASSED
"""
#non-test function
"""
def TC1():
    print("testcase1 function")
def TC2():
    print("testcase2 function")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items
"""
##################################################################################################
#class and method level
#non-testclass and test method
"""
class Sample:
    def test_m1(self):
        print("method1 testcase")
    def test_m2(self):
        print("method2 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items
"""
#testclass and test method
"""
class TestSample:
    def test_m1(self):
        print("method1 testcase")
    def test_m2(self):
        print("method2 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 2 items

pytestconcept.py::TestSample::test_m1 method1 testcase
PASSED
pytestconcept.py::TestSample::test_m2 method2 testcase
PASSED
"""
#testclass and non-test method
"""
class TestSample:
    def m1(self):
        print("method1 testcase")
    def m2(self):
        print("method2 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items
"""
#testclass and non-test method
"""
class TestSample:
    def test_m1(self):
        print("method1 testcase")
    def m2_test(self):
        print("method2 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 1 item

pytestconcept.py::TestSample::test_m1 method1 testcase
PASSED
"""
##########################################################################################
#class level
"""
class TestSample:
    def test_m1(self):
        print("m1 testcase1")
    def test_m2(self):
        print("m2 testcase2")

class TestSimple:
    def test_m3(self):
        print("m3 testcase1")
    def test_m4(self):
        print("m4 testcase2")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::TestSample::test_m1 m1 testcase1
PASSED
pytestconcept.py::TestSample::test_m2 m2 testcase2
PASSED
pytestconcept.py::TestSimple::test_m3 m3 testcase1
PASSED
pytestconcept.py::TestSimple::test_m4 m4 testcase2
PASSED
"""
#non-test class andnon-test method
"""
class TestSample:
    def test_m1(self):
        print("m1 testcase1")
    def test_m2(self):
        print("m2 testcase2")

class SimpleTest:
    def test_m3(self):
        print("m3 testcase1")
    def test_m4(self):
        print("m4 testcase2")
"""
"""
>pytest -vs pytestconcept.py
collected 2 items

pytestconcept.py::TestSample::test_m1 m1 testcase1
PASSED
pytestconcept.py::TestSample::test_m2 m2 testcase2
PASSED
"""
#non-test class andnon-test method
"""
class TestSample:
    def test_m1(self):
        print("m1 testcase1")
    def m2(self):
        print("m2 testcase2")

class SimpleTest:
    def m3(self):
        print("m3 testcase1")
    def test_m4(self):
        print("m4 testcase2")
"""
"""
>pytest -vs pytestconcept.py
collected 1 item

pytestconcept.py::TestSample::test_m1 m1 testcase1
PASSED
"""
#test class consist of constructor
"""
class TestDemo:
    def __init__(self):
        print("im a constructor")
    def test_m1(self):
        print("m1 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items
 PytestCollectionWarning: cannot collect test class 'TestDemo'
because it has a __init__ constructor (from: pytestconcept.py)
"""
############################################################################################
#module level
"""
def test_fun1():
    print("testcase function")

class TestGmail:
    def test_compose(self):
        print("compos testcase")
    def test_inbox(self):
        print("inbox testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_fun1 testcase function
PASSED
pytestconcept.py::TestGmail::test_compose compos testcase
PASSED
pytestconcept.py::TestGmail::test_inbox inbox testcase
PASSED
"""