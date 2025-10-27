"""
fixtures
"""
"""
def outer(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner

@outer
def fun():
    ...
fun()
"""
"""
def check_data(func):
    def inner(*args, **kwargs):
        print("check for internet and VPN connection")
        func(*args, **kwargs)
    return inner
@check_data         #tc1 = check_data(tc1)
def tc1():
    print("testcase1")
@check_data
def tc2():
    print("testcase2")
@check_data
def tc3():
    print("testcase3")
    """
# tc1()
# tc2()
# tc3()
# check for internet and VPN connection
# testcase1
# check for internet and VPN connection
# testcase2
# check for internet and VPN connection
# testcase3
"""
*according to above example there are 3 testcase are present, we should decorate for all 3 function and we should
call manually all 3 functions,so code length will get increase to avoid this we go for fixtures.
"""
"""
fixture:
--------
*fixture is a kind of decorator,it will execute before and after each test function/class/module.
*fixture should be marked with "@pytest.fixture" for fixture function.
*fixture(decorator function) should not start with "test" keyword.(it can start with test keyword but it is not recommended)
*we can use/call fixture in 2 ways,
1.we can call fixture manually in each test function/method, by specifying fixture name as a "1st argument" in each 
test function/method.
2.by using "autouse=True" keyword argument it will applies for all function and method.(no need to manually
calling the fixture)

syntax:
-------
@pytest.fixture
def func():
    ...
    yield
    ...

def test_tc1(func):
    ...

*the order of execution is 1st fixture will execute, then control will given to test_function and test function will
execute, then control give to yield.

autouse
*******
*in the above example we are not passing fixture name as an argument to test function, in this case, fixture
will not execute, to over come this drawback, without even passing the fixture name it should use automatically for
all the test function that case we should pass "autouse=True" as an argumnet.
*by default "autouse=False"(will be in False state)
*by default scope of fixture/autouse will be for function level.

yield
=====
*we have a scenario that before and after each function/class/module a fixture should execute, then in this case
we use "yield" keyword.

*"yield" will pause the execution and it will give control where the function been called, after function execution
again control will give to yield, after yield what ever present it will execute and control give to next function.

note:
-----
*fixture can starts with test keyword, but dont start with test keyword, because we will get confusion
"""
#######################################################################################################
#function level fixture
#fixture without yield
"""
@pytest.fixture
def outer():
    print("check for internet connect")

def test_testcase1(outer):
    print("testcase1")

def test_testcase2(outer):
    print("testcase2")
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::test_testcase1 check for internet connect
testcase1
PASSED
pyconcept.py::test_testcase2 check for internet connect
testcase2
PASSED
"""

"""
@pytest.fixture
def outer():
    print("check for internet connect")

def test_testcase1(outer):
    print("testcase1")

def test_testcase2():
    print("testcase2")
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::test_testcase1 check for internet connect
testcase1
PASSED
pyconcept.py::test_testcase2 testcase2
PASSED  
"""

"""
@pytest.fixture
def outer():
    print("check for internet connect")
    yield
    print("off internet")

def test_testcase1(outer):
    print("testcase1")

def test_testcase2(outer):
    print("testcase2")
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::test_testcase1 check for internet connect
testcase1
PASSEDoff internet

pyconcept.py::test_testcase2 check for internet connect
testcase2
PASSEDoff internet
"""

"""
@pytest.fixture
def outer1():
    print("check for internet connection")
    yield
    print("off internet")
@pytest.fixture
def outer2():
    print("check for server connection")
    yield
    print("off server")

def test_testcase1(outer1, outer2):
    print("testcase1")

def test_testcase2(outer1, outer2):
    print("testcase2")
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::test_testcase1 check for internet connection
check for server connection
testcase1
PASSEDoff server
off internet

pyconcept.py::test_testcase2 check for internet connection
check for server connection
testcase2
PASSEDoff server
off internet
"""

"""
@pytest.fixture
def outer1():
    print("check for internet connection")
    yield
    print("off internet")
@pytest.fixture
def outer2():
    print("check for server connection")
    yield
    print("off server")

@pytest.mark.smoke
def test_testcase1(outer1, outer2):
    print("testcase1")

def test_testcase2(outer1, outer2):
    print("testcase2")
"""
"""
>pytest -vs -m "smoke" pyconcept.py
collected 2 items / 1 deselected / 1 selected

pyconcept.py::test_testcase1 check for internet connection
check for server connection
testcase1
PASSEDoff server
off internet
"""
#################################################################################################################
#function level with autouse
"""
@pytest.fixture(autouse=True)
def instal():
    print("instal build")
    yield
    print("uninstal build")

def test_login():
    print("testcase on login")
def test_signup():
    print("testcase on signup")
def test_reels():
    print("testcase on reels")
def test_story():
    print("testcase on story")
"""
"""
>pytest -vs pyconcept.py
collected 4 items

pyconcept.py::test_login instal build
testcase on login
PASSEDuninstal build

pyconcept.py::test_signup instal build
testcase on signup
PASSEDuninstal build

pyconcept.py::test_reels instal build
testcase on reels
PASSEDuninstal build

pyconcept.py::test_story instal build
testcase on story
PASSEDuninstal build
"""
"""
note:
*****
*in fixture method also consider as a function only.
*when we set "autouse=True" both function level and method level will get execute automatically.
"""

"""
@pytest.fixture
def instal():
    print("instal build")
    yield
    print("uninstal build")

def test_login(instal):
    print("testcase on login")
def test_signup():
    print("testcase on signup")
def test_reels(instal):
    print("testcase on reels")
def test_story():
    print("testcase on story")
"""
"""
>pytest -vs pyconcept.py
collected 4 items

pyconcept.py::test_login instal build
testcase on login
PASSEDuninstal build

pyconcept.py::test_signup testcase on signup
PASSED
pyconcept.py::test_reels instal build
testcase on reels
PASSEDuninstal build

pyconcept.py::test_story testcase on story
PASSED
"""

"""
@pytest.fixture()
def instal():
    print("instal build")
    yield
    print("uninstal build")

class Test_Insta:
    def test_login(self, instal):
        print("testcase on login")
    def test_signup(self):
        print("testcase on signup")
    def test_reels(self, instal):
        print("testcase on reels")
    def test_story(self):
        print("testcase on story")
"""
"""
collected 4 items

pyconcept.py::Test_Insta::test_login instal build
testcase on login
PASSEDuninstal build

pyconcept.py::Test_Insta::test_signup testcase on signup
PASSED
pyconcept.py::Test_Insta::test_reels instal build
testcase on reels
PASSEDuninstal build

pyconcept.py::Test_Insta::test_story testcase on story
PASSED
"""

"""
@pytest.fixture(autouse=True)
def instal():
    print("instal build")
    yield
    print("uninstal build")

class Test_Insta:
    def test_login(self):
        print("testcase on login")
    def test_signup(self):
        print("testcase on signup")
    def test_reels(self):
        print("testcase on reels")
    def test_story(self):
        print("testcase on story")
"""
"""
>pytest -vs pyconcept.py
collected 4 items

pyconcept.py::Test_Insta::test_login instal build
testcase on login
PASSEDuninstal build

pyconcept.py::Test_Insta::test_signup instal build
testcase on signup
PASSEDuninstal build

pyconcept.py::Test_Insta::test_reels instal build
testcase on reels
PASSEDuninstal build

pyconcept.py::Test_Insta::test_story instal build
testcase on story
PASSEDuninstal build
"""
############################################################################################################
#method level
"""
@pytest.fixture
def instal():
    print("instal build")
    yield
    print("uninstal build")

@pytest.mark.usefixtures("instal")
class Test_Insta:
    def test_login(self):
        print("testcase on login")
    def test_signup(self):
        print("testcase on signup")

@pytest.mark.usefixtures("instal")
class Test_FB:
    def test_reels(self):
        print("testcase on reels")
    def test_story(self):
        print("testcase on story")
"""
"""
>pytest -vs pyconcept.py
collected 4 items

pyconcept.py::Test_Insta::test_login instal build
testcase on login
PASSEDuninstal build

pyconcept.py::Test_Insta::test_signup instal build
testcase on signup
PASSEDuninstal build

pyconcept.py::Test_FB::test_reels instal build
testcase on reels
PASSEDuninstal build

pyconcept.py::Test_FB::test_story instal build
testcase on story
PASSEDuninstal build
"""
#############################################################################################################
#class level
"""
scope="class"
*************
->before each class it will execute one time.
"""
"""
@pytest.fixture(scope="class", autouse=True)
def instal():
    print("instal build")
    yield
    print("uninstal build")

class Test_Insta:
    def test_login(self):
        print("testcase on login")
    def test_signup(self):
        print("testcase on signup")

class Test_FB:
    def test_reels(self):
        print("testcase on reels")
    def test_story(self):
        print("testcase on story")
"""
"""
>pytest -vs pyconcept.py
collected 4 items

pyconcept.py::Test_Insta::test_login instal build
testcase on login
PASSED
pyconcept.py::Test_Insta::test_signup testcase on signup
PASSEDuninstal build

pyconcept.py::Test_FB::test_reels instal build
testcase on reels
PASSED
pyconcept.py::Test_FB::test_story testcase on story
PASSEDuninstal build
"""
####################################################################################################################
#module levele
"""
scope="module"
**************
->before all function/class it will execute one time.
"""
"""
pytestmark = pytest.mark.usefixtures("setup")

@pytest.fixture()
def setup():
    print("before")
    yield
    print("end")

def test_tc1():
    print("tescase1")

class Test_FB:
    def test_reels(self):
        print("testcase on reels")
    def test_story(self):
        print("testcase on story")
"""
"""
>pytest -vs pyconcept.py
collected 3 items

pyconcept.py::test_tc1 before
tescase1
PASSEDend

pyconcept.py::Test_FB::test_reels before
testcase on reels
PASSEDend

pyconcept.py::Test_FB::test_story before
testcase on story
PASSEDend
"""

"""
pytestmark = pytest.mark.usefixtures("setup")

@pytest.fixture(scope="module")
def setup():
    print("before")
    yield
    print("end")

def test_tc1():
    print("tescase1")

class Test_FB:
    def test_reels(self):
        print("testcase on reels")
    def test_story(self):
        print("testcase on story")
"""
"""
collected 3 items

pyconcept.py::test_tc1 before
tescase1
PASSED
pyconcept.py::Test_FB::test_reels testcase on reels
PASSED
pyconcept.py::Test_FB::test_story testcase on story
PASSEDend
"""
########################################################################################################################
"""
@pytest.fixture(autouse=True)
def greet():
    print("welcome")
    yield
    print("end")

def test_TC1():
    print("testcase1")
def test_TC2():
    print("testcase2")
def test_TC3():
    print("testcase3")
"""
"""
collected 3 items

conftest.py::test_TC1 welcome
testcase1
PASSEDend

conftest.py::test_TC2 welcome
testcase2
PASSEDend

conftest.py::test_TC3 welcome
testcase3
PASSEDend
"""

"""
*according to above example when we write autouse="True" with scope="function" then a fixture will get
execute for all the function, but we want a fixture to be execute only for a particular 
function/method/module/class then we use "@pytest.mark.usefixtures("fixture_name")" marker.

*usefixtures:
-------------
*it is a built-in marker will be marked for a particular class/module to execute a fixture.

note:
-----
*for function/method if we specify the fixture name as an argument then it will work similar to "usefixtures" marker.
"""
#############################################################################################################
"""
callling multiple fixture:
**************************
*when ever we are calling multiple fixture, it will execute all the fixture in order then function/class/module
will get execute.

@pytest.fixture
def fix1():
    stmt1
    yield
    stmt2
@pytest.fixture
def fix2():
    stmt3
    yield
    stmt4

def func1(fix1, fix2):
    stmt5

order of execution:
--------------------
<----before yield------->     function   ---->after yield<----    
stmt1(fix1)-->stmt3(fix2)-->stmt5(func1)-->stmt4(fix2)-->stmt2(fix1)

"""
#multiple fixtures for single function manually calling(without yield)
"""
@pytest.fixture
def fix1():
    print("start1")
@pytest.fixture
def fix2():
    print("start2")

def test_tc1(fix1,fix2):
    print("testcase1")
"""
"""
collected 1 item

conftest.py::test_tc1 start1
start2
testcase1
PASSED
"""
################################################################################################################
"""
params:
=======
*when we want to execute fixture for multiple of set of i/p then we use "params" as a keyword argument.
*params will always accept iterable.

@pytest.fixture(params=iterable)
def fix:
    ...

def test_func1(fix):
    ...

note:
-----
no.of execution of fixture = no. of elements in params
"""
#function level
#fixture with parameter without yield
"""
@pytest.fixture(autouse=True, params=["id1", "id2", "id3"])
def wish():
    print("welcome")

def test_tc1():
    print("testcase1")

def test_tc2():
    print("testcase2")
"""
"""
collected 6 items

pyconcept.py::test_tc1[id1] welcome
testcase1
PASSED
pyconcept.py::test_tc1[id2] welcome
testcase1
PASSED
pyconcept.py::test_tc1[id3] welcome
testcase1
PASSED
pyconcept.py::test_tc2[id1] welcome
testcase2
PASSED
pyconcept.py::test_tc2[id2] welcome
testcase2
PASSED
pyconcept.py::test_tc2[id3] welcome
testcase2
PASSED
"""

"""
@pytest.fixture(autouse=True, params=["id1", "id2", "id3"])
def wish():
    print("welcome")
    yield
    print("end")

def test_tc1():
    print("testcase1")

def test_tc2():
    print("testcase2")
"""
"""
collected 6 items

pyconcept.py::test_tc1[id1] welcome
testcase1
PASSEDend

pyconcept.py::test_tc1[id2] welcome
testcase1
PASSEDend

pyconcept.py::test_tc1[id3] welcome
testcase1
PASSEDend

pyconcept.py::test_tc2[id1] welcome
testcase2
PASSEDend

pyconcept.py::test_tc2[id2] welcome
testcase2
PASSEDend

pyconcept.py::test_tc2[id3] welcome
testcase2
PASSEDend
"""
######################################################################################################################
#method level
"""
@pytest.fixture(autouse=True, params=["id1", "id2", "id3"])
def wish():
    print("welcome")
    yield
    print("end")

class Test_Facebook:
    def test_tc1(self):
        print("testcase1")
class Test_Insta:
    def test_tc2(self):
        print("testcase2")
"""
"""
collected 6 items

pyconcept.py::Test_Facebook::test_tc1[id1] welcome
testcase1
PASSEDend

pyconcept.py::Test_Facebook::test_tc1[id2] welcome
testcase1
PASSEDend

pyconcept.py::Test_Facebook::test_tc1[id3] welcome
testcase1
PASSEDend

pyconcept.py::Test_Insta::test_tc2[id1] welcome
testcase2
PASSEDend

pyconcept.py::Test_Insta::test_tc2[id2] welcome
testcase2
PASSEDend

pyconcept.py::Test_Insta::test_tc2[id3] welcome
testcase2
PASSEDend
"""
#####################################################################################################################
#class level
"""
@pytest.fixture(autouse=True, scope="class", params=["id1", "id2"])
def wish():
    print("welcome")
    yield
    print("end")

class Test_Insta:
    def test_tc2(self) :
        print("testcase2")
    def test_tc3(self):
        print("testcase3")
"""
"""
collected 4 items

pyconcept.py::Test_Insta::test_tc2[id1] welcome
testcase2
PASSED
pyconcept.py::Test_Insta::test_tc3[id1] testcase3
PASSED
pyconcept.py::Test_Insta::test_tc2[id2] end
welcome
testcase2
PASSED
pyconcept.py::Test_Insta::test_tc3[id2] testcase3
PASSEDend
"""
######################################################################################################################
"""
utilizing parameters(params) inside a fixture:
***********************************************
*to use parameters inside a fixture we should write "request" as an argument in fixture.
*to utilize inside a fixture function we should write "request.param".

synatx:
-------
@pytest.fixture(params="iterables")
def fixture_name(request):
    request.param

"""

#parameters inside a fixture
"""
@pytest.fixture(autouse=True, params=["id1", "id2"])
def wish(request):
    print("welcome")
    print(f"the input is {request.param}")

def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")
"""
"""
collected 4 items

pyconcept.py::test_tc2[id1] welcome
the input is id1
testcase2
PASSED
pyconcept.py::test_tc2[id2] welcome
the input is id2
testcase2
PASSED
pyconcept.py::test_tc3[id1] welcome
the input is id1
testcase3
PASSED
pyconcept.py::test_tc3[id2] welcome
the input is id2
testcase3
PASSED
"""

"""
@pytest.fixture(autouse=True, params=[4563, 6745, 2345, 7812, 1234])
def wish(request):
    print("welcome")
    if request.param<3000:
        print(f"the ID-{request.param} for regression")

def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")
"""
"""
collected 10 items

pyconcept.py::test_tc2[4563] welcome
testcase2
PASSED
pyconcept.py::test_tc2[6745] welcome
testcase2
PASSED
pyconcept.py::test_tc2[2345] welcome
the ID-2345 for regression
testcase2
PASSED
pyconcept.py::test_tc2[7812] welcome
testcase2
PASSED
pyconcept.py::test_tc2[1234] welcome
the ID-1234 for regression
testcase2
PASSED
pyconcept.py::test_tc3[4563] welcome
testcase3
PASSED
pyconcept.py::test_tc3[6745] welcome
testcase3
PASSED
pyconcept.py::test_tc3[2345] welcome
the ID-2345 for regression
testcase3
PASSED
pyconcept.py::test_tc3[7812] welcome
testcase3
PASSED
pyconcept.py::test_tc3[1234] welcome
the ID-1234 for regression
testcase3
PASSED
"""

#parameters inside a fixture
"""
@pytest.fixture(params=[["demo","demo@123"], ["sample", "sample@123"], ["log", "log@123"]])
def wish(request):
    print("Welcome")
    print(request.param)
    yield
    print("End")

def test_tc1(wish):
    print("Testcase1")
"""
"""
collected 3 items

conftest.py::test_tc1[wish0] Welcome
['demo', 'demo@123']
Testcase1
PASSEDEnd

conftest.py::test_tc1[wish1] Welcome
['sample', 'sample@123']
Testcase1
PASSEDEnd

conftest.py::test_tc1[wish2] Welcome
['log', 'log@123']
Testcase1
PASSEDEnd
"""

#parameters inside a fixture with condition
"""
@pytest.fixture(params=[["demo","demo@123"], ["sample", "sample@123"], ["log", "log@123"]])
def wish(request):
    if len(request.param[0])>=4:        #["demo","demo@123"]  len(demo)>=4 T len(sample)>=4 T  len(log)>=4 F
        print("Welcome")
        print(f"Valid username is {request.param[0]}")
    yield
    print("End")

def test_tc1(wish):
    print("Testcase1")
"""
"""
collected 3 items

conftest.py::test_tc1[wish0] Welcome
Valid username is demo
Testcase1
PASSEDEnd

conftest.py::test_tc1[wish1] Welcome
Valid username is sample
Testcase1
PASSEDEnd

conftest.py::test_tc1[wish2] Testcase1
PASSEDEnd
"""

######################################################################################################################
"""
parameters present in fixture accessing in test function:
*********************************************************
*a value present in fixture to access inside a test function/method we should return a value by "yield" stmt.
*then call the fixture inside a test function/method, it will return some value and store it in a variable and
access it.

syntax:
-------
@pytest.fixture(params="iterables")
def fix_name(request):
    yield request.param

def test_fun(fix_name):
    var_name = fix_name

note:
*we can't write autouse=True when we are returning/yielding a value
"""
#example on accessing a value from one function inside a another function
"""
def add():
    a = 10
    return a
def sub():
    b = 5
    a = add()
    print(a - b)
"""

#parameters inside a test function
"""
@pytest.fixture(params=["mozila", "chrome", "ie"])
def wish(request):
    print("welcome")
    yield request.param

def test_tc1(wish):
    a = wish
    print(a)
    print("testcase1")
"""
"""
collected 3 items

pyconcept.py::test_tc1[mozila] welcome
mozila
testcase1
PASSED
pyconcept.py::test_tc1[chrome] welcome
chrome
testcase1
PASSED
pyconcept.py::test_tc1[ie] welcome
ie
testcase1
PASSED
"""

#example on returning local variable in test function
"""
@pytest.fixture
def wish():
    ip = "123.567.678.0.0"
    print("welcome")
    yield ip

def test_tc1(wish):
    ip = wish
    print(ip)
    print("testcase1")
"""
"""
collected 1 item

pyconcept.py::test_tc1 welcome
123.567.678.0.0
testcase1
PASSED
"""
