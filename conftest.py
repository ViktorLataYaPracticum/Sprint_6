import pytest
from selenium import webdriver
from urls import Urls

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.SERVICE_URL)
    yield driver
    driver.quit()
