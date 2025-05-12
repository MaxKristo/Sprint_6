import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators

# класс содержит методы главной страницы и наследует базовые методы
class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

#Кликаем на вопрос
    @allure.step('Кликаем на вопрос')
    def click_to_question(self, num):
         question_locator = self.format_locator(MainPageLocators.question_locator, num)
         self.scroll_to_element(MainPageLocators.last_question_locator_to_scroll)
         self.click_to_element(question_locator)

#Получаем текст ответа
    @allure.step('Получаем текст ответа')
    def get_answer_text(self, num):
         answer_locator = self.format_locator(MainPageLocators.answer_locator, num)
         return self.get_text_from_element(answer_locator)

# принятие куки, клик по кнопке "Заказать" в теле на главной странице
    @allure.step('Переход в форме заказа при клике кнопки "Заказать" в теле на главной странице')
    @allure.description('Принять куки, клик по кнопке "Заказать" в теле на главной странице и подтверждение перехода к форме "Заказать"')
    def click_button_order_in_body_of_main_page_and_transition_to_order_page(self):
        self.close_cookies()
        self.click_to_element(MainPageLocators.button_order_locator)
        self.find_element(OrderPageLocators.fields_name_locator)

# метод закрытие окна с куками
    @allure.step('Закрытие окна с куками')
    def close_cookies(self):
        cookie_close_button = self.wait.until(expected_conditions.element_to_be_clickable(BasePageLocators.button_accept_cookie_locator))
        cookie_close_button.click()

# принятие куки, клик по кнопке "Заказать" в заголовке
    @allure.step('Переход в форме заказа при клике кнопки "Заказать" в хедере')
    @allure.description('Принять куки, клик по кнопке "Заказать" в хедере и подтверждение перехода к форме "Заказать"')
    def click_order_button_in_header_and_transition_to_order_page(self):
        self.close_cookies()
        self.click_to_element(BasePageLocators.button_order_header_locator)
        self.find_element(OrderPageLocators.fields_name_locator)
