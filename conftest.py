from selenium import webdriver
import pytest

from pages.order_page import OrderPage
from urls import Urls
from pages.main_page import MainPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.base_url)
    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(Urls.base_url)
    return page

@pytest.fixture()
def order_page(driver):
    page = OrderPage(driver)
    page.go_to_url(Urls.order_url)
    return page