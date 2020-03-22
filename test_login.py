from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import driver
from model.user import User

def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to.alert.accept()

def login(driver, user):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user.username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(user.password)
    driver.find_element_by_name("submit").click()

def test_login(driver):
    driver.get("http://localhost/php4dvd/")
    login(driver, User.Admin())
    logout(driver)

