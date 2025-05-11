from urls import Urls
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Инициализация Firefox WebDriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.base_url)
    yield driver
    driver.quit()