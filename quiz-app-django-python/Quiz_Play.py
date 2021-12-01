from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

username = "n123"
password = "n123"

#driver = webdriver.Chrome("/Users/yashvimehta/Downloads/chromedriver")
driver = webdriver.Chrome("./chromedriver")
driver.get("http://127.0.0.1:8000/login")
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("submit").click()
driver.find_element_by_id("btn").click()
driver.find_element_by_id("start-quiz").click()
driver.find_element_by_id("start_attempt_quiz").click()
driver.find_element_by_id("IPL 2021 Phase 2 started on?-September 19").click()
driver.find_element_by_id("In the IPL 2015, which bowler won the Purple Cap?-Bhuvneshwar Kumar").click()
driver.find_element_by_id("Who won IPL in 2021-Chennai Super Kings").click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element_by_id("Who was the first batsman to score a century in the IPL?-Virendra Sehwag")
driver.find_element_by_id("Who among the following teams did not reach the semi finals of IPL 2008?-Delhi Daredevils")
driver.find_element_by_id("How many English bowlers have taken a five-wicket haul in the IPL?-1")
driver.find_element_by_id("Which of these IPL franchise was banned for two years?-Chennai Super Kings").click()
driver.find_element_by_id("Which among these cities has hosted the most number of IPL matches?-Bangalore").click()
driver.find_element_by_id("Which season(s) had the most number of hat-tricks?-2014").click()
driver.find_element_by_id("Who was the captain of the Mumbai Indians in IPL 2012?-Rohit Sharma").click()
driver.find_element_by_id("button1").click()

print(driver.current_url())
if("http://127.0.0.1:8000/" ==driver.current_url()):
    print("no error")

driver.close()