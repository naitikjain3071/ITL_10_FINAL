from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

firstname = "chinmay"
lastname = "jain"
email = "chinmaycj7@gmail.com"
username = "chinmay1234"
password = "chinmay1234"

# driver = webdriver.Chrome("/Users/yashvimehta/Downloads/chromedriver")
driver = webdriver.Chrome("./chromedriver")
driver.get("http://127.0.0.1:8000/signup")

driver.find_element_by_id("first_name").send_keys(firstname)
driver.find_element_by_id("last_name").send_keys(lastname)
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("password1").send_keys(password)
driver.find_element_by_id("password2").send_keys(password)
driver.find_element_by_id("submit").click()

print(driver.getCurrentUrl())
if("http://127.0.0.1:8000/" ==driver.getCurrentUrl()):
    print("no error")

driver.close()