"""
handling frames:
----------------
*a webpage inside another webpage is called as frames/nested frames/embedded webpage.
*to develop a frame developer will use <iframe> tag.
*by default control will present in parent webpage, we need to switch control from
parent to child webpage will use following method.
    driver.switch_to.frame(arg)
*frame() method will accept 3 different types of arguments,
    *index : starts from 0
    *name : name attribute value
    *webelement : address of a frame
*to switch control from child to parent there are 2 methods are present,
    driver.switch_to.parent_frame() -->it switch from child to its own parent
    driver.switch_to.default_content() ->it will switch from child to main parent(ancestor)
*frame() method is an example for polymorphism.
*if argument(index/name/webelement) is not matches then it will throw "NoSuchFrameException" 
"""
#ws to enter hello in UN1 and bye in UN2
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
#NoSuchElementException
#according to above script the control is present in parent webpage, we need to switch 
control from parent to child webpage.
"""
#ws to enter hello in UN1, bye in UN2, good in UN3 by using index as argument
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
driver.switch_to.frame(0)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
driver.switch_to.frame(0)
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
"""
#ws to enter hello in UN1, bye in UN2, good in UN3 by using name as argument
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
driver.switch_to.frame("n1")
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
driver.switch_to.frame("n2")
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
"""
#ws to enter hello in UN1, bye in UN2, good in UN3 by using webelement as argument
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
frame1 = driver.find_element("xpath", "//iframe[@id='f1']")
driver.switch_to.frame(frame1)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
frame2 = driver.find_element("xpath", "//iframe[@id='f2']")
driver.switch_to.frame(frame2)
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
"""
#example on switching control from child to its own parent
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
frame1 = driver.find_element("xpath", "//iframe[@id='f1']")
driver.switch_to.frame(frame1)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
frame2 = driver.find_element("xpath", "//iframe[@id='f2']")
driver.switch_to.frame(frame2)
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
driver.switch_to.parent_frame()
un2.send_keys("back to parent")
"""
#example on switching control from child to main parent(ancestor)
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
frame1 = driver.find_element("xpath", "//iframe[@id='f1']")
driver.switch_to.frame(frame1)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
frame2 = driver.find_element("xpath", "//iframe[@id='f2']")
driver.switch_to.frame(frame2)
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
driver.switch_to.default_content()
un1.send_keys("back to main parent")
"""

#ws to click on sign up with google in x.com
"""
driver = Chrome(options=o)
driver.get("https://x.com/")
driver.maximize_window()
sleep(5)
ele = driver.find_element("xpath", "//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(ele)
driver.find_element("xpath", "(//span[.='Sign up with Google'])[1]").click()
"""