import selenium
from selenium import webdriver
import time
 
  
driver = webdriver.Chrome()
driver.get("http://localhost/php4dvd/")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("admin")
time.sleep(3)
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("submit").click()
time.sleep(3)
driver.find_element_by_link_text("Log out").click()
time.sleep(3)
#driver.switch_to_alert().accept()
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()
