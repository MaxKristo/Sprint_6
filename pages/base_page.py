import allure
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import Urls

# класс содержит базовые методы
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

# метод принимает куки, если сообщение о куки появилось
    @allure.step('Принять куки')
    def accept_cookie(self):
        try:                # ожидание кнопки "да все привыкли"
            cookie_close_button = self.wait.until(expected_conditions.element_to_be_clickable(BasePageLocators.button_accept_cookie_locator))
            cookie_close_button.click()
        except:
            pass            # если кнопка не появилась, то продолжаем тест


# поиск элемента
    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 8).until(expected_conditions.presence_of_element_located(locator))

# клик по элементу
    @allure.step('Кликнуть элемент')
    def click_to_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

# скроллинг до элемента и ожидание его кликабельности
    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        return element

# получение текста из элемента
    @allure.step('Получаем текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

# метод передаёт тест элементу
    @allure.step('Изменить текст')
    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def format_locator(self, locator, text):
        by, locator_str = locator
        locator_str = locator_str.format(text)
        return by, locator_str

# при клике на логотип Яндекс, в новом окне через редирект откроется главная страница Дзена.
    @allure.step('Проверить переход при клике на логотип Яндекс в заголовке')
    @allure.description('При клике на логотип Яндекс, в новом окне через редирект откроется главная страница Дзена.')
    def click_to_logo_yandex_and_change_to_dzen(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.wait.until(expected_conditions.url_contains(Urls.dzen_url))

# принятие куки, клик по кнопке "Заказать" в заголовке
    @allure.step('Переход в форме заказа при клике кнопки "Заказать" в хедере')
    @allure.description('Принять куки, клик по кнопке "Заказать" в хедере и подтверждение перехода к форме "Заказать"')
    def click_order_button_in_header_and_transition_to_order_page(self):
        self.accept_cookie()
        self.click_to_element(BasePageLocators. button_order_header_locator)
        self.find_element(OrderPageLocators.fields_name_locator)

# метод получает текущий url
    @allure.step('Проверка URL')
    def check_to_url(self):
        return self.driver.current_url
