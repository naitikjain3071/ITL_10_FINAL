from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Github credentials
username = "yashvii_"
password = "1233456765"

# initialize the Chrome driver
driver = webdriver.Chrome("/Users/yashvimehta/Downloads/chromedriver")
# head to github login page
driver.get("http://127.0.0.1:8000/login")
# find username/email field and send the username itself to the input field
driver.find_element_by_id("username").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(password)
# click login button
driver.find_element_by_id("submit").click()
# wait the ready state to be complete
# WebDriverWait(driver=driver, timeout=10).until(
#     lambda x: x.execute_script("return document.readyState === 'complete'")
# )
# error_message = "Incorrect username or password."
# # get the errors (if there are)
# errors = driver.find_elements_by_class_name("flash-error")
# # print the errors optionally
# # for e in errors:
# #     print(e.text)
# # if we find that error message within errors, then login is failed
# if any(error_message in e.text for e in errors):
#     print("[!] Login failed")
# else:
#     print("[+] Login successful")

# # close the driver

if("http://127.0.0.1:8000/" ==driver.getCurrentUrl()):
    print("no error")

driver.close()