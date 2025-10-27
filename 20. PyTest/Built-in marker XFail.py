"""
XFail
=====
 mark test functions as expected to fail
 You can use the xfail marker to indicate that you expect a test to fail:
Syntax: @pytest.mark.xfail([parameters])

1. condition parameter : If a test is only expected to fail under a certain condition, you can pass
that condition as the first parameter:
Eg:
@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_function():
    . . .

2. reason parameter: You can specify the motive of an expected failure with
the reason parameter
Eg:
@pytest.mark.xfail(reason="known parser issue")
def test_function():
    . . .

3. raises parameter: If you want to be more specific as to why the test is failing, you can specify
a single exception, or a tuple of exceptions, in the raises argument.
Eg:
@pytest.mark.xfail(raises=RuntimeError)
def test_function():
    . . .
note:
*****
*this marker will go when intenstaionally we want to fail the testcase because a feature is not stable/
new feature/not implemented/open defect/reqt changes etc..
*it will not print "fail" in result it will print as "xpass".
"""

"""
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail
def test_channel():
    print("channel module")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_chat chat module
PASSED
pytestconcept.py::test_status status module
PASSED
pytestconcept.py::test_channel channel module
XPASS
"""

"""
brw = "IE"
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail(brw in ["mozilla","chrome", "IE"], reason="not implemented")
def test_channel():
    print("channel module")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_chat chat module
PASSED
pytestconcept.py::test_status status module
PASSED
pytestconcept.py::test_channel channel module
XPASS (not implemented)
"""

"""
brw = "safari"
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail(brw in ["mozilla","chrome", "IE"], reason="not implemented")
def test_channel():
    print("channel module")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_chat chat module
PASSED
pytestconcept.py::test_status status module
PASSED
pytestconcept.py::test_channel channel module
PASSED
"""
"""
note:
*****
*in xfail marker if cond the is True then the result is "xpass" else if the cond is False the result
is "PASSED".
"""