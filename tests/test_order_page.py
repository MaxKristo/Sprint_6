import allure
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import User, order_confirm
from urls import Urls
from conftest import driver


class TestOrderPage:

    @allure.title('Заказ скутера кнопкой "Заказать" в заголовке')
    def test_place_order_page_by_click_on_order_button_in_the_header(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_button_in_header_and_transition_to_order_page()
        order_page.fill_form_who_is_the_scooter_for(User.user_1)
        order_page.fill_form_about_rent(User.user_1)
        order_page.click_to_element(OrderPageLocators. button_yes_locator)
        confirmation_text = order_page.get_text_from_element(OrderPageLocators.window_confirmation_order_locator)
        assert order_confirm in confirmation_text


    @allure.title('Заказ скутера кнопкой "Заказать" в теле"')
    def test_place_order_page_by_click_on_order_button_in_the_middle_of_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_button_order_in_body_of_main_page_and_transition_to_order_page()
        order_page = OrderPage(driver)
        order_page.fill_form_who_is_the_scooter_for(User.user_2)
        order_page.fill_form_about_rent(User.user_2)
        order_page.click_to_element(OrderPageLocators.button_yes_locator)
        confirmation_text = order_page.get_text_from_element(OrderPageLocators.window_confirmation_order_locator)
        assert order_confirm in confirmation_text


    @allure.title('Редирект на главную страницу «Самоката», при нажатии на логотип «Самокат» после оформления заказа')
    def test_click_on_the_scooter_logo_after_placing_an_order(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_button_in_header_and_transition_to_order_page()
        order_page.fill_form_who_is_the_scooter_for(User.user_1)
        order_page.fill_form_about_rent(User.user_1)
        order_page.click_to_element(OrderPageLocators.button_yes_locator)
        order_page.click_to_element(OrderPageLocators.button_view_status_locator)
        order_page.click_to_element(BasePageLocators.button_scooter_locator)
        assert order_page.check_to_url() == Urls.base_url


    @allure.title('Редирект в новом окне на главную страницу "Дзен", при нажатии на логотип "Яндекс" после оформления заказа')
    def test_click_on_the_yandex_logo_after_placing_an_order(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_button_in_header_and_transition_to_order_page()
        order_page.fill_form_who_is_the_scooter_for(User.user_2)
        order_page.fill_form_about_rent(User.user_2)
        order_page.click_to_element(OrderPageLocators.button_yes_locator)
        order_page.click_to_element(OrderPageLocators.button_view_status_locator)
        order_page.click_to_element(BasePageLocators.button_yandex_locator)
        order_page.click_to_logo_yandex_and_change_to_dzen()
        assert order_page.check_to_url() == Urls.dzen_url