from selenium import webdriver
import pytest

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver

