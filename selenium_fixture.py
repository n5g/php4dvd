from selenium import webdriver
import pytest
from model.application import Application

@pytest.fixture(scope="module") #без этой пометки фикстура будет инициальзироваться перед каждой функцией(короче чтоб двайвер
                                #инициализировался,прогнал все тестыа потом уже закрылся
#                               #по умолчанию scope="function"
def app(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return Application(driver)

