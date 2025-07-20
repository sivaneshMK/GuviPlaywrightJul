import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    yield driver
    driver.quit()

@pytest.fixture
def get_driver(driver):
    return driver
