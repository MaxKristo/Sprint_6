import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators

# класс содержит методы страницы заказа и наследует базовые методы
class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

# клик по полю и ввод в него значения
    @allure.title('Клик по полю и его заполнение')
    def fill_text_field(self, locator, text):
        self.click_to_element(locator)
        self.set_text(locator, text)

# заполнение формы "Для кого самокат"
    @allure.title('Заполнение формы "Для кого самокат"')
    @allure.description('Заполнение полей - "Имя", "Фамилия", "Адрес", "Телефон" и выбор из выпадающего списка станции метро "Пушкинская"')
    def fill_form_who_is_the_scooter_for(self, user):
        self.fill_text_field(OrderPageLocators.fields_name_locator, user["name"])
        self.fill_text_field(OrderPageLocators.fields_last_name_locator, user["surname"])
        self.fill_text_field(OrderPageLocators.fields_address_locator, user["address"])
        self.click_to_element(OrderPageLocators.fields_metro_station_locator)
        self.click_to_element(OrderPageLocators.fields_metro_station_1_locator)
        self.fill_text_field(OrderPageLocators.fields_telephone_locator, user["phone"])
        self.click_to_element(OrderPageLocators.button_next_locator)

# заполнение формы "Про аренду"
    @allure.title('Заполнение формы "Про аренду"')
    @allure.description('Заполнение поля - "Комментарий" и выбор "Даты начала аренды" из календаря, "Срока аренды" из выпадающего списка и выбор цвета самоката в чек боксе')
    def fill_form_about_rent(self, user):
        self.click_to_element(OrderPageLocators.field_date_locator)
        self.click_to_element(OrderPageLocators.choose_rent_day_locator)
        self.click_to_element(OrderPageLocators.field_rental_period_locator)
        self.click_to_element(OrderPageLocators.choose_rent_period_locator)
        self.click_to_element(OrderPageLocators.choose_black_color_locator)
        self.fill_text_field(OrderPageLocators.field_comment_locator, user["comment"])
        self.click_to_element(OrderPageLocators.button_place_order_locator)

# Соглашаемся на оформление заказа
    @allure.step('Соглашаемся на оформление заказа')
    def accept_window_yes(self):
        self.find_element(OrderPageLocators.button_yes_locator).click()

# Получение статуса заказа
    @allure.step('Получение статуса заказа')
    def getting_the_order_status(self):
        self.find_element(OrderPageLocators.button_view_status_locator).click()

# клик по лого "Самокат"
    @allure.step('клик по лого "Самокат"')
    def click_on_the_scooter_logo(self):
        self.find_element(BasePageLocators.button_scooter_locator).click()

# клик по лого "Яндекс"
    @allure.step('клик по лого "Яндекс"')
    def click_on_the_yandex_logo(self):
        self.find_element(BasePageLocators.button_yandex_locator).click()

    @allure.step('Проверка оформленного заказа')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.window_confirmation_order_locator)