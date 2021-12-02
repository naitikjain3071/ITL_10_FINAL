from logging import error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# Login credentials
username = "admin"
password = "admin"

# Details of Question
question_text ="What does HTML stand for?"



# initialize the Chrome driver
#driver = webdriver.Chrome("/Users/yashvimehta/Downloads/chromedriver")
driver = webdriver.Chrome("./chromedriver")

# Page URL
driver.get("http://127.0.0.1:8000/login")

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("submit").click()
driver.find_element_by_id("navbarDarkDropdownMenuLink").click()
driver.find_element_by_xpath("//a[@href='/add_question/']").click()

driver.find_element_by_id("id_content").send_keys(question_text)
driver.find_element_by_id("navbarDarkDropdownMenuLink").click()
select = Select(driver.find_element_by_id('id_quiz'))
# select by visible text
select.select_by_visible_text('Internet Technology')
# select by value 
select.select_by_value('13')
driver.find_element_by_class_name("btn").click()

if("http://127.0.0.1:8000/" ==driver.current_url):
    print("no error")

print('============================================')
print('TEST CASE PASSED')
print('============================================')

driver.close()