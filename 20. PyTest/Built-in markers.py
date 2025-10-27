"""
built-in markers:
----------------
1.skip
2.skipif
3.xfail
4.parameterize
5.usefixture
"""
"""
Skipping test functions
1. Skip
 The simplest way to skip a test function is to mark it with the skip decorator which may 
be passed an optional reason:
   @pytest.mark.skip(reason=””) : skips the testcases always without any reason
2. Skipif
  If you wish to skip something conditionally then you can use skipif instead.
  @pytest.mark.skipif(condition, reason): skips the testcases only when the condition is  True.
"""
#function level
"""
def test_tc1():
    print("testcase1")
@pytest.mark.skip
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")
@pytest.mark.skip
def test_tc4():
    print("testcase4")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::test_tc1 testcase1
PASSED
pytestconcept.py::test_tc2 SKIPPED (unconditional skip)
pytestconcept.py::test_tc3 testcase3
PASSED
pytestconcept.py::test_tc4 SKIPPED (unconditional skip)
"""

"""
def test_tc1():
    print("testcase1")
@pytest.mark.skip(reason="low priority")
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")
@pytest.mark.skip(reason="not important")
def test_tc4():
    print("testcase4")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::test_tc1 testcase1
PASSED
pytestconcept.py::test_tc2 SKIPPED (low priority)
pytestconcept.py::test_tc3 testcase3
PASSED
pytestconcept.py::test_tc4 SKIPPED (not important)
"""
#############################################################################################
"""
class TestSample:
    def test_tc1(self):
        print("testcase1")
    @pytest.mark.skip(reason="low priority")
    def test_tc2(self):
        print("testcase2")
    def test_tc3(self):
        print("testcase3")
    @pytest.mark.skip(reason="not important")
    def test_tc4(self):
        print("testcase4")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::test_tc1 testcase1
PASSED
pytestconcept.py::test_tc2 SKIPPED (low priority)
pytestconcept.py::test_tc3 testcase3
PASSED
pytestconcept.py::test_tc4 SKIPPED (not important)
"""

"""
@pytest.mark.skip(reason="all method are not required")
class TestSample:
    def test_tc1(self):
        print("testcase1")
    def test_tc2(self):
        print("testcase2")
class TestSimple:
    def test_tc3(self):
        print("testcase3")
    def test_tc4(self):
        print("testcase4")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::TestSample::test_tc1 SKIPPED (all method are not required)
pytestconcept.py::TestSample::test_tc2 SKIPPED (all method are not required)
pytestconcept.py::TestSimple::test_tc3 testcase3
PASSED
pytestconce
"""
#################################################################################################
#example on skipif
"""
testid = 3423
def test_TC1():
    print("testcas1")
@pytest.mark.skipif(testid in [5671, 2233, 3423, 7890], reason="test_case not required")
def test_TC2():
    print("testcas2")
def test_TC3():
    print("testcas3")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_TC1 testcas1
PASSED
pytestconcept.py::test_TC2 SKIPPED (test_case not required)
pytestconcept.py::test_TC3 testcas3
PASSED
"""

"""
testid = 3428
def test_TC1():
    print("testcas1")
@pytest.mark.skipif(testid in [5671, 2233, 3423, 7890], reason="test_case not required")
def test_TC2():
    print("testcas2")
def test_TC3():
    print("testcas3")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_TC1 testcas1
PASSED
pytestconcept.py::test_TC2 testcas2
PASSED
pytestconcept.py::test_TC3 testcas3
PASSED
"""

"""
class TestExe:
    os = "mac"
    def test_TC1(self):
        print("testcas1")
    @pytest.mark.skipif(os in ["linux", "window", "mac"], reason="platform missmatch")
    def test_TC2(self):
        print("testcas2")
    def test_TC3(self):
        print("testcas3")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::TestExe::test_TC1 testcas1
PASSED
pytestconcept.py::TestExe::test_TC2 SKIPPED (platform missmatch)
pytestconcept.py::TestExe::test_TC3 testcas3
PASSED
"""
"""
browser="IE"
class TestDemo:
    def test_Tc1(self):
        print("method1 testcase")
    def test_Tc2(self):
        print("method2 testcase")
@pytest.mark.skipif(browser=="IE", reason="IE not exists")
class TestSample:
    def test_Tc3(self):
        print("method3 testcase")
    def test_Tc4(self):
        print("method4 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::TestDemo::test_Tc1 method1 testcase
PASSED
pytestconcept.py::TestDemo::test_Tc2 method2 testcase
PASSED
pytestconcept.py::TestSample::test_Tc3 SKIPPED (IE not exists)
pytestconcept.py::TestSample::test_Tc4 SKIPPED (IE not exists)
"""