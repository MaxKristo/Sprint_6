from selenium import webdriver
import pytest
from urls import Urls

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.base_url)
    yield driver
    driver.quit()