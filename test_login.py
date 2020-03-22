from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app
from model.user import User

def test_login(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.logout()

