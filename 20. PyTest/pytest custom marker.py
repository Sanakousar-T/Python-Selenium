"""
markers:
--------
*markers are used to execute the specific test function/method/class/module.
*pytest markers are classified into 2 types,
    1.custom markers
    2.built-in markers

Pytest custom markers
=====================
 @pytest.mark is a decorator used to add the metadata to the test.
 Metadata : details about the data.
Grouping test cases using custom markers
 We can create custom markers by using, @pytest.mark.markerName
 We can group the test cases.
 To execute: pytest filename.py –vs –m “name of the marker”

 To execute multiple markers:
o pytest filename.py –vs –m “marker1 or marker2”  executes testcases which are
marked with either marker1 or marker2
o pytest filename.py –vs –m “marker1 and marker2”  executes the testcases which are
marked with both marker1 and marker2.
o pytest filename.py –vs –m “not marker2”  executes the testcases which are not
marked with marker2.
"""
# function level
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
def test_trash():
    print("tash testcase")
@pytest.mark.smoke
def test_compose():
    print("compose testcase")
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "smoke" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::test_login loginpage testcase
PASSED
pytestconcept.py::test_compose compose testcase
PASSED
"""
# executing which are marked with p3
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
def test_trash():
    print("tash testcase")
@pytest.mark.smoke
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "p3" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::test_trash tash testcase
PASSED
pytestconcept.py::test_bin bin testcase
PASSED
"""
# executing which are marked with smoke
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.smoke
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "smoke" pytestconcept.py
collected 4 items / 1 deselected / 3 selected

pytestconcept.py::test_login loginpage testcase
PASSED
pytestconcept.py::test_trash tash testcase
PASSED
pytestconcept.py::test_compose compose testcase
PASSED
"""
# executing which are marked with regression
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.smoke
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "regression" pytestconcept.py
collected 4 items / 4 deselected / 0 selected
"""
# example on writing multiple marker name
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "reg, smoke" pytestconcept.py
collected 4 items
ERROR: Wrong expression passed to '-m': reg, smoke: at column 4: unexpected character ","
"""
# executing smoke and p3 marker
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "smoke and p3" pytestconcept.py
collected 4 items / 3 deselected / 1 selected

pytestconcept.py::test_trash tash testcase
PASSED
"""
# executing smoke or reg marker
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "smoke or reg" pytestconcept.py
collected 4 items / 1 deselected / 3 selected

pytestconcept.py::test_login loginpage testcase
PASSED
pytestconcept.py::test_trash tash testcase
PASSED
pytestconcept.py::test_compose compose testcase
PASSED
"""
# executing excluding m3 marker
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "not p3" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::test_login loginpage testcase
PASSED
pytestconcept.py::test_compose compose testcase
PASSED
"""
#################################################################################################
# method level
# executing only regression marker
"""
class TestInsta:
    @pytest.mark.regression
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    def test_chat(self):
        print("chat testcase")
"""
"""
>pytest -vs -m "regression" pytestconcept.py
collected 3 items / 1 deselected / 2 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_chat chat testcase
PASSED
"""
# executing only regression marker
"""
class TestInsta:
    @pytest.mark.regression
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    def chat(self):
        print("chat testcase")
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "regression" pytestconcept.py
collected 3 items / 2 deselected / 1 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
"""
# executinh regression and high marker
"""
class TestInsta:
    @pytest.mark.regression
    @pytest.mark.high
    def test_post(self):
        print("post testcase")
    @pytest.mark.critical
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    @pytest.mark.low
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.high
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "regression and high" pytestconcept.py
collected 4 items / 3 deselected / 1 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
"""
# executinh regression or high marker
"""
class TestInsta:
    @pytest.mark.regression
    @pytest.mark.high
    def test_post(self):
        print("post testcase")
    @pytest.mark.critical
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    @pytest.mark.low
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.high
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "regression or high" pytestconcept.py
collected 4 items / 1 deselected / 3 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_chat chat testcase
PASSED
pytestconcept.py::TestInsta::test_register register testcase
PASSED
"""
##############################################################################################
# class level
# executinh which are marked with imp
"""
@pytest.mark.imp
class TestInsta:
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    def test_chat(self):
        print("chat testcase")
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "imp" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_story story testcase
PASSED
"""
# executinh which are marked with imp
"""
@pytest.mark.imp
class TestInsta:
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    def test_chat(self):
        print("chat testcase")
@pytest.mark.imp
class TestSample:
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "imp" pytestconcept.py
collected 4 items / 1 deselected / 3 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_story story testcase
PASSED
pytestconcept.py::TestSample::test_register register testcase
PASSED
"""
# executing class except mark with imp
"""
@pytest.mark.imp
class TestInsta:
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    def test_chat(self):
        print("chat testcase")
@pytest.mark.imp
class TestSample:
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "not imp" pytestconcept.py
collected 4 items / 3 deselected / 1 selected

pytestconcept.py::TestFb::test_chat chat testcase
PASSED
"""
# combination of class level and method level marker
"""
@pytest.mark.imp
class TestInsta:
    @pytest.mark.m1
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    @pytest.mark.m2
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.m1
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "m1" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestFb::test_register register testcase
PASSED
"""
# combination of class level and method level marker
"""
@pytest.mark.imp
class TestInsta:
    @pytest.mark.m1
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    @pytest.mark.m2
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.m1
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "imp" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_story story testcase
PASSED
"""

# single function multiple markers
"""
@pytest.mark.m1
@pytest.mark.m2
@pytest.mark.m3
@pytest.mark.m4
@pytest.mark.m5
@pytest.mark.m6
def test_chat():
    print("chat testcase")
"""
"""
>pytest -vs -m "m5" pytestconcept.py
collected 1 item

pytestconcept.py::test_chat chat testcase
PASSED
"""
################################################################################################
# module level
# marking for entire module
"""
pytestmark = pytest.mark.smoke

def test_fun1():
    print("funtion testcase")

class TestSample:
    def test_tc1(self):
        print("test method1")
    def test_tc2(self):
        print("test method2")
"""
"""
>pytest -vs -m "smoke" pytestconcept.py
collected 3 items

pytestconcept.py::test_fun1 funtion testcase
PASSED
pytestconcept.py::TestSample::test_tc1 test method1
PASSED
pytestconcept.py::TestSample::test_tc2 test method2
PASSED
"""