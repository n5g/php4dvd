from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app
from model.user import User

def test_login_valid(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.logout()

def test02_login_invalid(app):
    app.go_to_home_page()
    app.login(User.random())

