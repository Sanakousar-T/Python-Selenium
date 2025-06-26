"""
handling popup's
----------------
*a popup is a small window/small tab.
*popups are classified into 5 types,
1.alert and confirmation/java script popup
2.hidden division popup
3.file upload popup
4.file download popup
5.child browser popup
"""
#1.alert and confirmation/java script popup
"""
*a popup which consisting of "OK/Cancel" button thn it is called as alert and confirmation popup.
*it is classified into 2 types,
1.simple alert : a alert which consist of either "OK"/"Cancel" button.
2.alert and confirmation : a alert which consist of both "OK and Cancel" button.

*to automate alert and confirmation popup, first we need to switch control from webpage
 to alert.
*we use below method for handling alert,
    driver.switch_to.alert
*to click on OK button we use accept()
*to click on Cancel button we use dismiss()

characteristics of alert and confirmation:
-----------------------------------------
*we can't inspect the popup
*we can't move/drag the popup

note:
-----
we can't use both accept() and dismiss() method for single alert, if we use then it will
throw "NoAlertPresentException".
"""
#ws to handle simple alert
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//input[@value='Search']").click()
a = driver.switch_to.alert
a.accept()
"""
#ws to click on ok button in alert and confirmartion popup
"""
driver = Chrome(options=o)
driver.get("https://licindia.in/")
driver.maximize_window()
driver.find_element("xpath", "//a[@title='Login']").click()
a = driver.switch_to.alert
a.accept()
"""
#ws to click on cancel button in alert and confirmartion popup
"""
driver = Chrome(options=o)
driver.get("https://licindia.in/")
driver.maximize_window()
driver.find_element("xpath", "//a[@title='Login']").click()
a = driver.switch_to.alert
a.dismiss()
"""
#example on using both accept and dismiss method
"""
driver = Chrome(options=o)
driver.get("https://licindia.in/")
driver.maximize_window()
driver.find_element("xpath", "//a[@title='Login']").click()
a = driver.switch_to.alert
a.accept()
a.dismiss()
#NoAlertPresentException
"""
#ws to prin text of a popup
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//input[@value='Search']").click()
a = driver.switch_to.alert
print(a.text)
#Please enter some search keyword
"""
#######################################################################################
#2.hidden division popup
"""
*initially a popup will be hidden, if we perform any action then a popup will be appear 
this is called as hidden division popup.
*will automate this popup by find_element(), click(), send_keys() methods.

characteristics of alert and confirmation:
-----------------------------------------
*we can inspect the popup
*we can't move/drag the popup
"""
#ws to signin in isrtc
"""
driver = Chrome(options=o)
driver.get("https://www.irctc.co.in/nget/profile/user-registration")
driver.maximize_window()
driver.find_element("xpath", "//strong[.='SIGN IN']").click()
sleep(2)
driver.find_element("xpath", "(//input[@placeholder='User Name'])[2]").send_keys("selenium")
driver.find_element("xpath", "(//input[@type='password'])[3]").send_keys("selenium@123")
"""
#ws to generate a otp in mamaearth
"""
driver = Chrome(options=o)
driver.get("https://mamaearth.in/")
driver.maximize_window()
driver.find_element("xpath", "//div[.='Login']").click()
sleep(2)
driver.find_element("xpath", "//input[@type='number']").send_keys("9988776655")
driver.find_element("xpath", "//button[.='Login with OTP']").click()
"""
#######################################################################################
#3.file upload popup
"""
*uploading a file in webpage is called as file upload popup
*to automate this popup we use send_keys(r"path of a file")
*file upload popup should be developed by "input tag and type="file" attribute"

characteristics of alert and confirmation:
-----------------------------------------
*we can't inspect the popup
*we can move/drag the popup
"""
#ws to upload resume in naukri.com
"""
driver = Chrome(options=o)
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "(//h2[@class='main-3'])[1]").click()
driver.find_element("id", "resumeUpload").send_keys(r"C:\\Users\\Hp\\Desktop\\manual grooming notes.pdf")
"""
#ws to upload a file in pdf to word
"""
driver = Chrome(options=o)
driver.get("https://www.ilovepdf.com/pdf_to_word")
driver.maximize_window()
driver.find_element("xpath", "//input[@type='file']").send_keys(r"C:\\Users\\Hp\\Desktop\\manual grooming notes.pdf")
"""
#############################################################################################
#4.file download popup
"""
*downloading a file from a webpage is a called as file download popup.
*when ever we are downloading browser will think un-authorized person is downloading, 
it will not download, and default it will download in downloads folder, to over come 
this we use below code.

o = ChromeOptions()
o.add_experimental_option("prefs", {"safebrowsing.enabled":True,
                                    "download.default_directory":r"path of folder"})
"""
#ws to download python version from python.org(it will throw error)
"""
driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "(//a[.='Download Python 3.12.5'])[2]").click()
#unverified person is downloading, ON Safe Browsing
"""
#ws to download python version from python.org
"""
o = ChromeOptions()
o.add_experimental_option("prefs", {"safebrowsing.enabled":True})

driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "(//a[.='Download Python 3.12.5'])[2]").click()
sleep(9)
"""
#ws to download python version from python.org in specified location
"""
o = ChromeOptions()
o.add_experimental_option("prefs", {"safebrowsing.enabled":True,
                                    "download.default_directory":r"E:\\pythonnnn"})

driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "(//a[.='Download Python 3.12.5'])[2]").click()
sleep(19)
"""
#######################################################################################
#5.child browser popup
"""
*a browser inside another browser is called as child browser.
*by default a control will be present in parent window, we need to switch control
from parent to child window, by following method.
    syntax: driver.switch_to.window(window_address)
*to get the window address there are 2 property,
    1.driver.current_window_handle --> it will return only parent window address 
    2.driver.window_handles --> it will return list of parent followed by child window address
                            [parent, child1, child2, ... ] 
"""
#ws to click on settings in twitter page
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
driver.find_element("xpath", "//span[.='Settings']").click()
#NoSuchElementException
#because by default control will be present in parent webpage, we need to switch 
control from parent to child webpage.
"""
#example on parent and all child window address
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
pid = driver.current_window_handle
print(pid)              #51EA5808430D2C8BBCF32FD376D1D1C1
all_id = driver.window_handles
print(all_id)           #['51EA5808430D2C8BBCF32FD376D1D1C1', '112ADB9A56EF4AB26D37B08C74ED9E3F', 'A119BB326D867D39DA99587F74D55D48', '2B69761AF745A5CE41C37B7FA70F9D13']
"""
#ws to print all window title
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_id = driver.window_handles  #[parent, child1, child2, child3]
for i in all_id:                #i=parent
    driver.switch_to.window(i)  #switch_to.window(parent)
    sleep(5)
    print(driver.title)
# Demo Web Shop
# Google Workspace Updates: New community features for Google Chat and an update on Currents
# NopCommerce | Facebook
# nopCommerce (@nopCommerce) / X
"""
#ws to print all child window title
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_id = driver.window_handles      #[parent, child1, child2, child3]
for i in all_id[1:]:                #i=child1
    driver.switch_to.window(i)      #switch_to.window(child1)
    sleep(5)
    print(driver.title)
# NopCommerce | Facebook
# nopCommerce (@nopCommerce) / X
# Google Workspace Updates: New community features for Google Chat and an update on Currents
"""
#ws to close all windows one by one
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_id = driver.window_handles      #[parent, child1, child2, child3]
for i in all_id:                #i=child1
    driver.switch_to.window(i)      #switch_to.window(child1)
    sleep(2)
    driver.close()
"""
#ws to close all child window
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_id = driver.window_handles      #[parent, child1, child2, child3]
for i in all_id[1:]:                #i=child1
    driver.switch_to.window(i)      #switch_to.window(child1)
    sleep(2)
    driver.close()
"""
#ws to close only parent window
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
driver.close()
"""
#ws to click on settings in twitter page
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_ids = driver.window_handles     #allids=[parent, child1, child2, child3]
for i in all_ids:                   #i=parent
    driver.switch_to.window(i)      #switch_to.window(parent)
    sleep(4)
    if driver.title=="nopCommerce (@nopCommerce) / X":
        driver.find_element("xpath","//span[.='Settings']").click()
        break
"""
#ws to add a watch in add to cart in amazon
"""
driver = Chrome(options=o)
driver.get("https://www.amazon.in/s?k=watches+for+men&crid=KKROTQK9XU7G&sprefix=watc%2Caps%2C234&ref=nb_sb_ss_w_hit-vc-lth_watches-for-men_k0_1_4")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "(//span[contains(., 'Watch-BQ2492')])[3]").click()
all_ids = driver.window_handles     #all_ids = [parent, child]
driver.switch_to.window(all_ids[1]) #directly switching to child window
sleep(2)
driver.find_element("xpath", "//input[@id='add-to-cart-button']").click()
"""
