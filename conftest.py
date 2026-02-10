import allure
import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Constants.SERVICE_URL)
    yield driver
    driver.quit()
